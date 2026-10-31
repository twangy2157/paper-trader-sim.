#!/usr/bin/env python3
"""v3: pre-buy research gate + partial take-profit with trailing stop.
Paper only: no wallets, keys, RPC or orders. Builds on sniper_backtest_v2.py
(keep both files in the same folder).

Research gate (applied before any entry, using data known by minute 5):
  hard vetoes : mint + freeze authority not revoked, top-10 holders too big,
                developer holds too much
  soft score  : holder count, buy/sell ratio in first 5 min, has socials
Exits: hard stop-loss; sell tp1_frac at +tp1; trail the rest from its peak,
never below breakeven.

Features CSV: token,mint_revoked,freeze_revoked,top10_pct,dev_pct,holders,buy_sell,socials
Bars CSV: same as v2.

  python sniper_v3.py synth --n 3000 --info 1.0 --out bars.csv --feats-out feats.csv
  python sniper_v3.py run --data bars.csv --feats feats.csv
  python sniper_v3.py ablation --data bars.csv --feats feats.csv
"""
import argparse
import csv
import math
import random
import statistics
from dataclasses import dataclass, replace

from sniper_backtest_v2 import P, load, buy_px, sell_px, portfolio, metrics, show


@dataclass(frozen=True)
class P3(P):
    max_entry_age: int = 10       # features are known at minute 5
    min_entry_age: int = 5        # never enter before research data exists
    use_vetoes: int = 1
    max_top10: float = 40.0       # % of supply held by top 10 wallets
    max_dev: float = 10.0         # % held by developer
    min_score: float = 0.5
    require_features: int = 1     # skip tokens with no research data
    tp1: float = 1.0              # first take-profit at +100%
    tp1_frac: float = 0.5         # fraction sold there (1.0 = old full exit)
    trail: float = 0.25           # trailing stop on the remainder


def num(x):
    try:
        return float(x) if x not in (None, "") else None
    except ValueError:
        return None


def load_features(path):
    out = {}
    with open(path) as f:
        for r in csv.DictReader(f):
            out[r["token"]] = {
                "mint_revoked": num(r["mint_revoked"]),
                "freeze_revoked": num(r["freeze_revoked"]),
                "top10": num(r["top10_pct"]), "dev": num(r["dev_pct"]),
                "holders": num(r["holders"]), "buy_sell": num(r["buy_sell"]),
                "socials": num(r["socials"])}
    return out


def research(f, p):
    """Return (allowed, score). Unknown values are treated as failures."""
    if f is None:
        return (not p.require_features), 0.5
    if p.use_vetoes:
        checks = (f["mint_revoked"] == 1, f["freeze_revoked"] == 1,
                  f["top10"] is not None and f["top10"] <= p.max_top10,
                  f["dev"] is not None and f["dev"] <= p.max_dev)
        if not all(checks):
            return False, 0.0
    s = (0.4 * min((f["holders"] or 0) / 200, 1)
         + 0.4 * min((f["buy_sell"] or 0) / 2, 1)
         + 0.2 * (f["socials"] or 0))
    return s >= p.min_score, s


def run_token(name, ts, bars, p, feats):
    rnd = random.Random(f"{p.seed}:{name}")
    r_fail, r_mev, r_honey = rnd.random(), rnd.random(), rnd.random()
    f = feats.get(name) if feats else None
    ok, score = research(f, p)
    if not ok:
        return None
    # freeze authority left on => much likelier you can't sell
    p_honey = p.honeypot_prob if f is None else (0.15 if f["freeze_revoked"] != 1 else 0.01)
    n = len(bars)
    if n < 3:
        return None
    p0 = bars[0][1]
    for i in range(n):
        age, px, liq, _, _ = bars[i]
        if age > p.max_entry_age:
            return None
        if (age < p.min_entry_age or liq < p.min_liq or px / p0 - 1 < p.min_mom
                or p.size > p.max_pool_frac * liq):
            continue
        j = i + p.latency
        if j >= n:
            return None
        fage, fpx, fliq, _, _ = bars[j]
        entry_ts = ts + fage
        if fliq < p.min_liq or r_fail < p.fail_prob:
            return {"token": name, "entry_ts": entry_ts, "exit_ts": entry_ts,
                    "hold": 0, "reason": "failed", "pnl": -p.tip_usd,
                    "ret": -p.tip_usd / p.size, "score": score}
        quote_in = p.size * (1 - p.dex_fee)
        entry = buy_px(fpx, fliq, quote_in)
        if r_mev < p.mev_prob:
            entry *= 1 + p.mev_cost
        qty = quote_in / entry

        qty_left, tp1_done, peak = qty, False, entry
        sells = []                      # (qty, spot price, pool liquidity)
        prev = last_close = fpx
        last_liq = fliq
        reason, hold = "timeout", 0
        end = min(n, j + 1 + p.max_hold)
        for k in range(j + 1, end):
            _, pk, lk, hk, lok = bars[k]
            hold = k - j
            last_close, last_liq = pk, lk
            if pk < prev * (1 - p.rug_drop) or lk < 0.1 * fliq:
                sells.append((qty_left, pk, lk))
                qty_left, reason = 0.0, "rug"
                break
            if not tp1_done:
                stop = entry * (1 - p.sl)
                if lok <= stop:         # stop wins ties
                    sells.append((qty_left, min(stop, pk), lk))
                    qty_left, reason = 0.0, "sl"
                    break
                if hk >= entry * (1 + p.tp1):
                    q = qty_left * p.tp1_frac
                    sells.append((q, entry * (1 + p.tp1), lk))
                    qty_left -= q
                    tp1_done, peak = True, hk
                    if qty_left <= 1e-12:
                        qty_left, reason = 0.0, "tp"
                        break
            else:
                stop = max(entry, peak * (1 - p.trail))
                if lok <= stop:
                    sells.append((qty_left, min(stop, pk), lk))
                    qty_left, reason = 0.0, "trail"
                    break
                peak = max(peak, hk)
            prev = pk
        if qty_left > 0:
            sells.append((qty_left, last_close, last_liq))

        if r_honey < p_honey:
            proceeds, reason = 0.0, "honeypot"
        else:
            proceeds = sum(q * sell_px(s, l, q * s) for q, s, l in sells)
            proceeds *= (1 - p.dex_fee) * (1 - p.sell_tax)
        pnl = proceeds - p.size - p.tip_usd * (1 + len(sells))
        return {"token": name, "entry_ts": entry_ts, "exit_ts": entry_ts + hold,
                "hold": hold, "reason": reason, "pnl": pnl, "ret": pnl / p.size,
                "score": score}
    return None


def backtest(tokens, p, feats):
    trades = [t for t in (run_token(n, ts, b, p, feats) for n, ts, b in tokens) if t]
    return portfolio(trades, p)


def synth(n, seed, path, feat_path, edge=0.0, info=1.0, minutes=120):
    """Synthetic launches + research features.
    info = how well research features predict outcomes (0 = useless, 1 = strong).
    That is an ASSUMPTION: real predictive power must be measured on real data.
    Price paths carry no momentum edge unless edge>0."""
    rnd = random.Random(seed)
    with open(path, "w", newline="") as fb, open(feat_path, "w", newline="") as ff:
        wb, wf = csv.writer(fb), csv.writer(ff)
        wb.writerow(["token", "launch_ts", "t_min", "price", "high", "low", "liq"])
        wf.writerow(["token", "mint_revoked", "freeze_revoked", "top10_pct",
                     "dev_pct", "holders", "buy_sell", "socials"])
        for i in range(n):
            liq0 = math.exp(rnd.uniform(math.log(3000), math.log(60000)))
            rug_at, run_len = rnd.randint(10, 80), rnd.randint(15, 40)
            px, rugged, kind = 1e-5, False, None
            for t in range(minutes):
                if t == 5:
                    early = px / 1e-5 - 1
                    rp = min(0.9, 0.05 + edge * max(0.0, min(early, 0.5)))
                    rest = 1 - rp
                    kind = rnd.choices(["runner", "rug", "dud"],
                                       [rp, rest * 0.2 / 0.95, rest * 0.75 / 0.95])[0]
                if t < 5:
                    mu, sd = 0.0, 0.06
                elif kind == "runner":
                    mu, sd = (0.015 if t < 5 + run_len else -0.01), 0.05
                else:
                    mu, sd = -0.004, 0.04
                op = px
                px *= math.exp(rnd.gauss(mu, sd))
                if kind == "rug" and t >= rug_at and not rugged:
                    px *= 0.03
                    rugged = True
                hi = max(op, px) * math.exp(abs(rnd.gauss(0, sd * 0.5)))
                lo = min(op, px) * math.exp(-abs(rnd.gauss(0, sd * 0.5)))
                liq = liq0 * 0.02 if rugged else liq0 * (px / 1e-5) ** 0.5
                wb.writerow([f"T{i}", i * 5, t, f"{px:.12g}", f"{hi:.12g}",
                             f"{lo:.12g}", f"{max(liq, 100):.2f}"])
            bad = rnd.random() < ((0.12 + 0.68 * info) if kind == "rug" else 0.12)
            mint = freeze = 1
            top10, dev = rnd.uniform(15, 35), rnd.uniform(0, 5)
            if bad:
                v = rnd.choice(["mint", "freeze", "top10", "dev"])
                if v == "mint":
                    mint = 0
                elif v == "freeze":
                    freeze = 0
                elif v == "top10":
                    top10 = rnd.uniform(45, 80)
                else:
                    dev = rnd.uniform(12, 40)
            run = kind == "runner"
            holders = rnd.uniform(20, 200) + (info * 150 if run else 0)
            bs = rnd.uniform(0.6, 1.6) + (info * 0.8 if run else 0)
            soc = int(rnd.random() < ((0.3 + 0.4 * info) if run else 0.3))
            wf.writerow([f"T{i}", mint, freeze, f"{top10:.1f}", f"{dev:.1f}",
                         f"{holders:.0f}", f"{bs:.2f}", soc])


def line(name, m):
    print(f"  {name:34s} trades={m['trades']:4d} win={m['win_rate']:5.1f}% "
          f"avg={m['avg_ret_pct']:7.2f}% ci={m.get('avg_ret_95ci_pct', 'n/a'):>14s} "
          f"ret_on_cap={m['return_on_capital_pct']:7.1f}% pf={m['profit_factor']}")


def ablation(tokens, feats, base):
    steps = [
        ("A  momentum only (v2-style)", dict(use_vetoes=0, min_score=0.0, require_features=0, tp1_frac=1.0)),
        ("B  + rug/honeypot vetoes", dict(use_vetoes=1, min_score=0.0, require_features=1, tp1_frac=1.0)),
        ("C  + research score >= min_score", dict(use_vetoes=1, require_features=1, tp1_frac=1.0)),
        ("D  + partial TP and trailing stop", dict(use_vetoes=1, require_features=1)),
    ]
    for name, kw in steps:
        p = replace(base, **kw)
        acc, sk = backtest(tokens, p, feats)
        line(name, metrics(acc, len(tokens), p, sk, ci=True))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("synth")
    s.add_argument("--n", type=int, default=3000)
    s.add_argument("--seed", type=int, default=7)
    s.add_argument("--edge", type=float, default=0.0)
    s.add_argument("--info", type=float, default=1.0)
    s.add_argument("--out", default="bars.csv")
    s.add_argument("--feats-out", default="feats.csv")
    for name in ("run", "ablation"):
        r = sub.add_parser(name)
        r.add_argument("--data", required=True)
        r.add_argument("--feats", required=True)
        r.add_argument("--trades-out")
        if name == "run":
            for fld, v in P3.__dataclass_fields__.items():
                r.add_argument(f"--{fld.replace('_', '-')}", type=type(v.default),
                               default=v.default)
    a = ap.parse_args()

    if a.cmd == "synth":
        synth(a.n, a.seed, a.out, a.feats_out, a.edge, a.info)
        print(f"wrote {a.out} and {a.feats_out}")
        return

    tokens, feats = load(a.data), load_features(a.feats)
    if a.cmd == "run":
        p = P3(**{f: getattr(a, f) for f in P3.__dataclass_fields__})
        acc, sk = backtest(tokens, p, feats)
        show("RESULTS", metrics(acc, len(tokens), p, sk, ci=True))
        if a.trades_out and acc:
            with open(a.trades_out, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(acc[0].keys()))
                w.writeheader()
                w.writerows(acc)
        return

    # untuned: fixed settings, scored only on the later half of launches
    test = tokens[len(tokens) // 2:]
    print(f"ABLATION on later half ({len(test)} tokens), settings NOT tuned")
    ablation(test, feats, P3())


if __name__ == "__main__":
    main()
