#!/usr/bin/env python3
"""Live PAPER trader for new memecoin pools. Simulation only.

It makes read-only GET requests to GeckoTerminal's public API and writes pretend
trades to CSV files. No wallet, no keys, no orders, no money. Every run is
stateless apart from the files in --out, so it suits a cron job (see
paper-trader.yml). Needs sniper_v3.py and sniper_backtest_v2.py next to it.

Why a watchlist: the free API 429s after only ~6 requests in 15 seconds, and
Solana creates pools so fast that the "newest pools" pages never reach pools
5-12 minutes old. So:
  1. every run reads the newest pools (2 pages) and adds the young ones (<5 min)
     to a WATCHLIST, remembering the price it first saw
  2. pools that are now 5-12 minutes old are judged with ONE direct lookup each:
       liquidity >= $5k, price up >= 10% since first seen, then research
       features (authorities, holders, dev %, socials)
  3. EVERY pool passing liquidity + momentum gets a simulated entry
       filter=1 : also passed the research rules and a bankroll slot was free
       filter=0 : "shadow" trade, kept to compare research against plain momentum
  4. open positions are resolved by replaying minute bars through the stop-loss /
     take-profit / rug / 60-minute-timeout rules used in the backtests
       filter=1 positions are checked every --check-every minutes
       filter=0 positions are resolved once, after their 60 minute window
  5. SUMMARY.md is rewritten

Requests are spaced --sleep seconds apart (default 7) and a run stops early,
saving its state, if it is still rate limited after one backoff.

Files in --out:
  ledger.csv      ENTRY / EXIT / FAILED rows, one per simulated event
  candidates.csv  every pool judged (or missed), raw features, and why
  state.json      watchlist, open positions, bankroll, pools already judged
  SUMMARY.md      results so far (filter=1 vs filter=0 vs all)

Simulated frictions are the v2/v3 ones: constant-product price impact, 1% DEX
fee, $0.50 tip per transaction, 15% failed buys, 25% sandwiched buys, honeypot
risk. They are assumptions, not measurements.

KNOWN LIMITS (read before trusting any number):
  * Momentum is measured from the price when the pool was first SEEN (under 5
    min old) to judging time, not from the first candle like the backtests.
  * The formats of mint_authority, freeze_authority and
    holders.distribution_percentage are guesses. Raw values are saved in
    candidates.csv so the parsing can be fixed. Unknown = veto, so a wrong guess
    leaves filter=1 empty (filter=0 still collects data).
  * Only a sample of launches is seen (the 40 newest pools each run).
  * OHLCV has no historical liquidity: exit liquidity is the pool's reserve at
    resolution time, and rugs are detected from price collapses.

  python paper_trader.py run --network solana --out paper_data
  python paper_trader.py summary --out paper_data
"""
import argparse
import csv
import json
import os
import random
import statistics
import time
import urllib.error
import urllib.request
from collections import Counter
from dataclasses import replace
from datetime import datetime, timezone

from sniper_backtest_v2 import buy_px, sell_px, boot_ci
from sniper_v3 import P3, research

HEADERS = {"Accept": "application/json;version=20230302",
           "User-Agent": "paper-trader/1.0 (simulation only)"}
LEDGER_COLS = ["ts", "event", "pool", "name", "filter", "price", "size_usd",
               "reason", "pnl_usd", "ret_pct", "cash_after", "note"]
CAND_COLS = ["evaluated_at", "pool", "name", "created_at", "age_min", "liq_usd",
             "first_price", "price", "momentum_pct", "buy_sell", "mint_raw",
             "freeze_raw", "mint_revoked", "freeze_revoked", "top10_pct", "dist_raw",
             "dev_pct", "holders", "socials", "is_honeypot", "gt_score", "score",
             "passed_research", "decision", "reason"]


class OutOfBudget(Exception):
    """Stop making requests this run (call budget used up)."""


class RateLimited(OutOfBudget):
    """Still HTTP 429 after one backoff: stop this run, keep the state."""


class Api:
    def __init__(self, base, max_calls, sleep, backoff):
        self.base, self.max_calls = base.rstrip("/"), max_calls
        self.sleep, self.backoff, self.calls = sleep, backoff, 0

    def get(self, path):
        if self.calls >= self.max_calls:
            raise OutOfBudget()
        self.calls += 1
        for attempt in (1, 2):
            try:
                req = urllib.request.Request(self.base + path, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=30) as r:
                    data = json.load(r)
                time.sleep(self.sleep)
                return data
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    if attempt == 1:
                        print(f"  429 rate limited, waiting {self.backoff:.0f}s")
                        time.sleep(self.backoff)
                        continue
                    raise RateLimited()
                raise


def num(x):
    try:
        return float(x) if x not in (None, "") else None
    except (TypeError, ValueError):
        return None


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def append_csv(path, cols, row):
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerow(row)


def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return list(csv.DictReader(f))


def authority_revoked(v, null_means):
    """1 = revoked (safe), 0 = still active (risky), None = unknown."""
    if v is None:
        return 1 if null_means == "revoked" else None
    if v in (False, "no", "No", "revoked", "none", "None"):
        return 1
    if v in (True, "yes", "Yes"):
        return 0
    if isinstance(v, str) and len(v) > 8:   # looks like an address => still active
        return 0
    return None


def top10_of(dist):
    for k, v in (dist or {}).items():
        lk = k.lower()
        if "top" in lk and "10" in lk:
            return num(v)
    return None


class Trader:
    def __init__(self, a, now):
        self.a, self.now = a, now
        self.now_ts = int(now.timestamp())
        self.p = replace(P3(), tp1_frac=1.0, max_entry_age=a.max_age)
        self.api = Api(a.base, a.max_calls, a.sleep, a.backoff)
        os.makedirs(a.out, exist_ok=True)
        self.ledger = os.path.join(a.out, "ledger.csv")
        self.cands = os.path.join(a.out, "candidates.csv")
        self.state_path = os.path.join(a.out, "state.json")
        if os.path.exists(self.state_path):
            with open(self.state_path) as f:
                self.state = json.load(f)
        else:
            self.state = {}
        self.state.setdefault("cash", self.p.capital)
        for k in ("decided", "open", "watch"):
            self.state.setdefault(k, {})

    # ---------- bookkeeping ----------
    def save(self):
        self.state["decided"] = {k: v for k, v in self.state["decided"].items()
                                 if self.now_ts - v < 7200}
        tmp = self.state_path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(self.state, f, indent=1)
        os.replace(tmp, self.state_path)

    def log(self, event, tag, **kw):
        row = {"ts": iso(self.now_ts), "event": event,
               "cash_after": round(self.state["cash"], 2)}
        row.update(tag)
        row.update(kw)
        append_csv(self.ledger, LEDGER_COLS, row)

    def cand(self, **kw):
        kw.setdefault("evaluated_at", iso(self.now_ts))
        append_csv(self.cands, CAND_COLS, kw)

    def pool_attrs(self, addr):
        return self.api.get(f"/networks/{self.a.network}/pools/{addr}")["data"]["attributes"]

    # ---------- watchlist ----------
    def expire_watch(self):
        """Pools never judged in time: record them and stop tracking."""
        for addr, w in list(self.state["watch"].items()):
            age = (self.now_ts - w["created"]) / 60
            if age > self.p.max_entry_age:
                del self.state["watch"][addr]
                self.state["decided"][addr] = self.now_ts
                self.cand(pool=addr, name=w["name"], created_at=iso(w["created"]),
                          age_min=round(age, 1), liq_usd=w["liq"], first_price=w["price"],
                          decision="skip", reason="missed_window")

    def refresh_watch(self):
        added = 0
        for page in range(1, self.a.pages + 1):
            try:
                data = self.api.get(f"/networks/{self.a.network}/new_pools?page={page}")["data"]
            except OutOfBudget:
                raise
            except Exception as e:
                print("  new_pools page", page, "failed:", e)
                break
            for pool in data:
                at = pool["attributes"]
                addr = at["address"]
                if addr in self.state["decided"] or addr in self.state["watch"]:
                    continue
                try:
                    created = parse_ts(at["pool_created_at"]).timestamp()
                except Exception:
                    continue
                age = (self.now_ts - created) / 60
                price = num(at.get("base_token_price_usd"))
                if price and price > 0 and -1 <= age < self.p.min_entry_age:
                    self.state["watch"][addr] = {
                        "name": at.get("name") or addr[:8], "created": created,
                        "price": price, "liq": num(at.get("reserve_in_usd"))}
                    added += 1
        print(f"  watchlist: +{added}, now {len(self.state['watch'])} pools")

    def due_watch(self):
        p = self.p
        out = [(w["created"], addr, w) for addr, w in self.state["watch"].items()
               if (self.now_ts - w["created"]) / 60 >= p.min_entry_age]
        out.sort(key=lambda x: x[0])          # oldest first: closest to expiring
        return out

    # ---------- exits ----------
    def replay(self, pos, bars):
        p, entry = self.p, pos["entry"]
        prev, last = pos["spot"], None
        for ts, _o, h, l, c in bars:
            if ts < pos["start"] or ts > pos["end"]:
                continue
            last = c
            if c < prev * (1 - p.rug_drop):
                return "rug", c, ts, last
            if l <= entry * (1 - p.sl):                 # stop wins ties
                return "sl", min(entry * (1 - p.sl), c), ts, last
            if h >= entry * (1 + p.tp1):
                return "tp", entry * (1 + p.tp1), ts, last
            prev = c
        return None, None, None, last

    def resolve(self, addr, pos):
        p, net = self.p, self.a.network
        limit = min(1000, max(5, (self.now_ts - pos["start"]) // 60 + 5))
        rows = self.api.get(f"/networks/{net}/pools/{addr}/ohlcv/minute"
                            f"?aggregate=1&limit={limit}")["data"]["attributes"]["ohlcv_list"]
        bars = sorted([int(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4])]
                      for r in rows)
        reason, spot, ts, last = self.replay(pos, bars)
        final = self.now_ts >= pos["end"] + 60
        if reason is None:
            if not final:
                pos["last_check"] = self.now_ts
                return False
            reason, spot, ts = "timeout", (last if last else pos["spot"]), pos["end"]
        cur_liq = None
        try:
            cur_liq = num(self.pool_attrs(addr).get("reserve_in_usd"))
        except OutOfBudget:
            raise
        except Exception as e:
            print("  liquidity lookup failed, using entry liquidity:", e)
        exit_liq = cur_liq if cur_liq else pos["liq"]
        if reason == "timeout" and cur_liq is not None and cur_liq < 0.1 * pos["liq"]:
            reason = "rug"
        if pos["r_honey"] < pos["p_honey"]:
            proceeds, reason = 0.0, "honeypot"
        else:
            proceeds = (pos["qty"] * sell_px(spot, exit_liq, pos["qty"] * spot)
                        * (1 - p.dex_fee) * (1 - p.sell_tax))
        pnl = proceeds - p.size - 2 * p.tip_usd
        if pos["selected"]:
            self.state["cash"] += p.size + pnl
        del self.state["open"][addr]
        self.log("EXIT", {"pool": addr, "name": pos["name"], "filter": int(pos["selected"])},
                 price=f"{spot:.12g}", size_usd=p.size, reason=reason,
                 pnl_usd=round(pnl, 2), ret_pct=round(100 * pnl / p.size, 2),
                 note=f"exit_bar={iso(ts)}")
        print(f"  EXIT  {pos['name'][:24]:24s} {reason:9s} pnl={pnl:8.2f} filter={int(pos['selected'])}")
        return True

    # ---------- entries ----------
    def fetch_features(self, addr, buy_sell):
        info = self.api.get(f"/networks/{self.a.network}/pools/{addr}/info")["data"]
        at = (info[0] if isinstance(info, list) else info)["attributes"]
        holders = at.get("holders") or {}
        dist = holders.get("distribution_percentage")
        nm = self.a.null_authority_means
        feats = {"mint_revoked": authority_revoked(at.get("mint_authority"), nm),
                 "freeze_revoked": authority_revoked(at.get("freeze_authority"), nm),
                 "top10": top10_of(dist), "dev": num(at.get("developer_holding_percentage")),
                 "holders": num(holders.get("count")), "buy_sell": buy_sell,
                 "socials": int(bool(at.get("twitter_handle") or at.get("telegram_handle")
                                     or at.get("websites")))}
        raw = {"mint_raw": json.dumps(at.get("mint_authority")),
               "freeze_raw": json.dumps(at.get("freeze_authority")),
               "dist_raw": json.dumps(dist), "is_honeypot": json.dumps(at.get("is_honeypot")),
               "gt_score": at.get("gt_score")}
        return feats, raw

    def judge(self, addr, w):
        p = self.p
        at = self.pool_attrs(addr)
        name = w["name"]
        age = (self.now_ts - w["created"]) / 60
        price, liq = num(at.get("base_token_price_usd")), num(at.get("reserve_in_usd"))
        base = {"pool": addr, "name": name, "created_at": iso(w["created"]),
                "age_min": round(age, 1), "liq_usd": liq, "price": price,
                "first_price": w["price"]}

        def done(decision, reason, **extra):
            self.state["watch"].pop(addr, None)
            self.state["decided"][addr] = self.now_ts
            self.cand(**base, decision=decision, reason=reason, **extra)

        if not price or price <= 0:
            return done("skip", "no_price")
        if liq is None or liq < p.min_liq:
            return done("skip", "low_liquidity")
        mom = price / w["price"] - 1
        base["momentum_pct"] = round(100 * mom, 1)
        if mom < p.min_mom:
            return done("skip", "no_momentum")
        if p.size > p.max_pool_frac * liq:
            return done("skip", "size_too_big_for_pool")

        m5 = (at.get("transactions") or {}).get("m5") or {}
        buy_sell = round(((m5.get("buys") or 0) + 1) / ((m5.get("sells") or 0) + 1), 3)
        try:
            feats, raw = self.fetch_features(addr, buy_sell)
        except OutOfBudget:
            raise
        except Exception as e:
            print("  features failed for", addr, e)
            feats, raw = None, {}
        ok, score = research(feats, p)
        if raw.get("is_honeypot") == "true":
            ok = False
        extra = dict(raw)
        if feats:
            extra.update(buy_sell=buy_sell, mint_revoked=feats["mint_revoked"],
                         freeze_revoked=feats["freeze_revoked"], top10_pct=feats["top10"],
                         dev_pct=feats["dev"], holders=feats["holders"],
                         socials=feats["socials"])
        extra.update(score=round(score, 3), passed_research=int(ok))

        slots = sum(1 for x in self.state["open"].values() if x["selected"])
        selected = bool(ok and slots < p.max_positions
                        and self.state["cash"] >= p.size + p.tip_usd)
        rnd = random.Random(addr)
        r_fail, r_mev, r_honey = rnd.random(), rnd.random(), rnd.random()
        tag = {"pool": addr, "name": name, "filter": int(selected)}
        if r_fail < p.fail_prob:
            if selected:
                self.state["cash"] -= p.tip_usd
            self.log("FAILED", tag, price=f"{price:.12g}", size_usd=0, reason="tx_failed",
                     pnl_usd=-p.tip_usd, ret_pct="", note="buy reverted, tip lost")
            return done("failed_tx", "simulated failed buy", **extra)

        quote_in = p.size * (1 - p.dex_fee)
        entry = buy_px(price, liq, quote_in)
        if r_mev < p.mev_prob:
            entry *= 1 + p.mev_cost
        qty = quote_in / entry
        start = (self.now_ts // 60 + 1) * 60
        p_honey = p.honeypot_prob if feats is None else (
            0.01 if feats["freeze_revoked"] == 1 else 0.15)
        if selected:
            self.state["cash"] -= p.size
        self.state["open"][addr] = {
            "name": name, "entry_ts": self.now_ts, "entry": entry, "qty": qty,
            "spot": price, "liq": liq, "selected": selected, "start": start,
            "end": start + p.max_hold * 60, "r_honey": r_honey, "p_honey": p_honey}
        why = "research_passed" if selected else (
            "research_failed" if not ok else "no_free_slot_or_cash")
        self.log("ENTRY", tag, price=f"{entry:.12g}", size_usd=p.size, reason=why,
                 note=f"score={score:.2f} momentum={100 * mom:.0f}%")
        print(f"  ENTRY {name[:24]:24s} filter={int(selected)} score={score:.2f}")
        done("enter" if selected else "shadow_enter",
             "research_passed" if selected else ("research_failed" if not ok else "no_slot"),
             **extra)

    # ---------- main loop ----------
    def run(self):
        a = self.a
        try:
            self.expire_watch()
            self.refresh_watch()
            for _, addr, w in self.due_watch():
                self.guarded(self.judge, addr, w)
            for addr, pos in list(self.state["open"].items()):
                last = pos.get("last_check", pos["entry_ts"])
                if pos["selected"] and self.now_ts - last >= a.check_every * 60:
                    self.guarded(self.resolve, addr, pos)
            for addr, pos in list(self.state["open"].items()):
                if not pos["selected"] and self.now_ts >= pos["end"] + 60:
                    self.guarded(self.resolve, addr, pos)
        except OutOfBudget as e:
            print("stopping early:", "still rate limited (429)" if isinstance(e, RateLimited)
                  else f"call budget ({a.max_calls}) reached")
        finally:
            self.save()
            write_summary(a.out)
        print(f"done: {self.api.calls} API calls, watch={len(self.state['watch'])}, "
              f"open={len(self.state['open'])}, cash={self.state['cash']:.2f}")

    def guarded(self, fn, *args):
        try:
            fn(*args)
        except OutOfBudget:
            raise
        except Exception as e:
            print(f"  {fn.__name__} failed: {e}")


# ---------- reporting ----------
def group_stats(label, exits, fails):
    rets = [float(r["ret_pct"]) for r in exits]
    pnl = sum(float(r["pnl_usd"]) for r in exits) + sum(float(r["pnl_usd"]) for r in fails)
    if not rets:
        return f"| {label} | 0 | - | - | - | {pnl:.2f} | {len(fails)} |"
    ci = ""
    if len(rets) > 5:
        lo, hi = boot_ci(rets)
        ci = f"[{lo:.1f}, {hi:.1f}]"
    wins = 100 * sum(r > 0 for r in rets) / len(rets)
    return (f"| {label} | {len(rets)} | {wins:.0f}% | {statistics.mean(rets):.1f}% | "
            f"{ci or '-'} | {pnl:.2f} | {len(fails)} |")


def write_summary(out):
    led = read_csv(os.path.join(out, "ledger.csv"))
    cands = read_csv(os.path.join(out, "candidates.csv"))
    state_path = os.path.join(out, "state.json")
    st = json.load(open(state_path)) if os.path.exists(state_path) else {}
    ex = [r for r in led if r["event"] == "EXIT"]
    fl = [r for r in led if r["event"] == "FAILED"]
    lines = ["# Paper trader summary", "", "SIMULATION ONLY. No real trades.", "",
             f"Updated {iso(time.time())}. Bankroll cash (research-selected trades): "
             f"{st.get('cash', 'n/a')}. Open positions: {len(st.get('open', {}))}. "
             f"Pools on watchlist: {len(st.get('watch', {}))}.", "",
             "| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |",
             "|---|---|---|---|---|---|---|",
             group_stats("filter=1 (research-selected)", [r for r in ex if r["filter"] == "1"],
                         [r for r in fl if r["filter"] == "1"]),
             group_stats("filter=0 (momentum only)", [r for r in ex if r["filter"] == "0"],
                         [r for r in fl if r["filter"] == "0"]),
             group_stats("all momentum entries", ex, fl), ""]
    n1 = sum(1 for r in ex if r["filter"] == "1")
    lines.append("Verdict: " + ("NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI "
                                "above zero before believing anything)." if n1 < 30 else
                                "check the CI column: only a lower bound above 0 is evidence."))
    if cands:
        c = Counter(r["reason"] for r in cands)
        lines += ["", f"Pools seen: {len(cands)}. Outcomes:", ""]
        lines += [f"- {k}: {v}" for k, v in c.most_common()]
        unk = sum(1 for r in cands if r["passed_research"] != "" and r["mint_revoked"] == "")
        if unk:
            lines += ["", f"Warning: {unk} judged pools had an unreadable mint/freeze value. "
                      "Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing."]
    with open(os.path.join(out, "SUMMARY.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--network", default="solana")
    r.add_argument("--out", default="paper_data")
    r.add_argument("--base", default="https://api.geckoterminal.com/api/v2")
    r.add_argument("--pages", type=int, default=2, help="pages of newest pools to read")
    r.add_argument("--max-calls", type=int, default=35)
    r.add_argument("--sleep", type=float, default=7.0, help="seconds between requests")
    r.add_argument("--backoff", type=float, default=65.0, help="wait after a 429")
    r.add_argument("--check-every", type=float, default=10, help="minutes between exit checks")
    r.add_argument("--max-age", type=int, default=12, help="latest pool age (min) to judge")
    r.add_argument("--now", help="ISO time override, for testing")
    r.add_argument("--null-authority-means", choices=["unknown", "revoked"], default="unknown")
    s = sub.add_parser("summary")
    s.add_argument("--out", default="paper_data")
    a = ap.parse_args(argv)
    if a.cmd == "summary":
        print(write_summary(a.out))
        return
    now = parse_ts(a.now) if a.now else datetime.now(timezone.utc)
    Trader(a, now).run()


if __name__ == "__main__":
    main()
