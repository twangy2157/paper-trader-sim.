#!/usr/bin/env python3
"""Paper-only memecoin sniper backtester, v2 (harsher, more realistic costs).

No wallets, no keys, no exchange or RPC calls, no orders. Reads a CSV of
historical per-minute bars for newly launched tokens and simulates entries.

CSV columns: token,launch_ts,t_min,price,liq   (+ optional high,low)
  launch_ts = launch time in minutes (used for ordering)
  t_min     = minutes since launch, contiguous from 0
  price     = bar close, liq = pool liquidity in USD (both sides)

What v2 models (v1 did not):
  * constant-product AMM price impact on every buy and sell
  * intrabar stop-loss / take-profit using high/low (stop wins ties)
  * failed/reverted buys that still cost a network tip
  * sandwich/MEV on some buys, honeypots you can't sell, optional sell tax
  * fixed per-transaction tip on top of the DEX fee
  * bankroll limit and max concurrent positions
  * bootstrap confidence interval on average return

Usage:
  python sniper_backtest_v2.py synth --n 3000 --out synth.csv [--edge 0]
  python sniper_backtest_v2.py run   --data synth.csv --trades-out trades.csv
  python sniper_backtest_v2.py sweep --data synth.csv
"""
import argparse
import csv
import heapq
import itertools
import math
import random
import statistics
from collections import defaultdict
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class P:
    min_liq: float = 5000.0       # skip pools thinner than this (USD)
    max_entry_age: int = 5        # only snipe within N minutes of launch
    min_mom: float = 0.10         # require +10% vs first bar before entering
    size: float = 100.0           # USD per trade
    latency: int = 1              # bars between signal and fill
    dex_fee: float = 0.01         # per side
    tip_usd: float = 0.50         # fixed network/priority cost per tx
    tp: float = 1.0               # take profit at +100%
    sl: float = 0.30              # stop loss at -30%
    max_hold: int = 60            # bars
    max_pool_frac: float = 0.05   # skip if size > 5% of pool liquidity
    fail_prob: float = 0.15       # buy reverts/fails: costs tip, no fill
    mev_prob: float = 0.25        # chance a buy gets sandwiched
    mev_cost: float = 0.03        # extra adverse price when sandwiched
    honeypot_prob: float = 0.03   # token can't be sold: total loss
    sell_tax: float = 0.0         # token-level tax on sells
    rug_drop: float = 0.80        # one-bar drop this big = rug
    capital: float = 1000.0       # bankroll
    max_positions: int = 5        # concurrent open positions
    seed: int = 1                 # seeds the random frictions


def load(path):
    toks = defaultdict(lambda: {"ts": 0, "bars": []})
    with open(path) as f:
        for r in csv.DictReader(f):
            px = float(r["price"])
            hi = float(r["high"]) if r.get("high") else px
            lo = float(r["low"]) if r.get("low") else px
            t = toks[r["token"]]
            t["ts"] = int(float(r["launch_ts"]))
            t["bars"].append((int(r["t_min"]), px, float(r["liq"]),
                              max(hi, px), min(lo, px)))
    out = []
    for k, v in toks.items():
        v["bars"].sort()
        out.append((k, v["ts"], v["bars"]))
    out.sort(key=lambda x: x[1])
    return out


def buy_px(spot, liq, quote_in):
    """Constant-product: average price paid for quote_in USD of tokens."""
    return spot * (1 + quote_in / max(liq / 2, 1.0))


def sell_px(spot, liq, value):
    """Constant-product: average price received selling `value` USD of tokens."""
    return spot / (1 + value / max(liq / 2, 1.0))


def run_token(name, ts, bars, p):
    rnd = random.Random(f"{p.seed}:{name}")
    r_fail, r_mev, r_honey = rnd.random(), rnd.random(), rnd.random()
    n = len(bars)
    if n < 3:
        return None
    p0 = bars[0][1]
    for i in range(n):
        age, px, liq, _, _ = bars[i]
        if age > p.max_entry_age:
            return None
        if (liq < p.min_liq or px / p0 - 1 < p.min_mom
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
                    "ret": -p.tip_usd / p.size}
        quote_in = p.size * (1 - p.dex_fee)
        entry = buy_px(fpx, fliq, quote_in)
        if r_mev < p.mev_prob:
            entry *= 1 + p.mev_cost
        qty = quote_in / entry

        prev = last_close = fpx
        last_liq = fliq
        reason, spot, exit_liq, hold = "timeout", None, None, 0
        end = min(n, j + 1 + p.max_hold)
        for k in range(j + 1, end):
            _, pk, lk, hk, lok = bars[k]
            hold = k - j
            last_close, last_liq = pk, lk
            if pk < prev * (1 - p.rug_drop) or lk < 0.1 * fliq:
                reason, spot, exit_liq = "rug", pk, lk
                break
            if lok <= entry * (1 - p.sl):          # stop first on ties
                reason, spot, exit_liq = "sl", min(entry * (1 - p.sl), pk), lk
                break
            if hk >= entry * (1 + p.tp):
                reason, spot, exit_liq = "tp", entry * (1 + p.tp), lk
                break
            prev = pk
        if spot is None:
            spot, exit_liq = last_close, last_liq

        if r_honey < p.honeypot_prob:
            proceeds, reason = 0.0, "honeypot"
        else:
            exec_px = sell_px(spot, exit_liq, qty * spot)
            proceeds = qty * exec_px * (1 - p.dex_fee) * (1 - p.sell_tax)
        pnl = proceeds - p.size - 2 * p.tip_usd
        return {"token": name, "entry_ts": entry_ts, "exit_ts": entry_ts + hold,
                "hold": hold, "reason": reason, "pnl": pnl, "ret": pnl / p.size}
    return None


def portfolio(trades, p):
    """Apply bankroll and concurrent-position limits in time order."""
    cash, open_pos, accepted, skipped = p.capital, [], [], 0
    for t in sorted(trades, key=lambda t: t["entry_ts"]):
        while open_pos and open_pos[0][0] <= t["entry_ts"]:
            cash += heapq.heappop(open_pos)[1]
        if t["reason"] == "failed":
            if cash < p.tip_usd:
                skipped += 1
                continue
            cash += t["pnl"]
            accepted.append(t)
            continue
        if len(open_pos) >= p.max_positions or cash < p.size + p.tip_usd:
            skipped += 1
            continue
        cash -= p.size
        heapq.heappush(open_pos, (t["exit_ts"], p.size + t["pnl"]))
        accepted.append(t)
    return accepted, skipped


def backtest(tokens, p):
    trades = [t for t in (run_token(n, ts, b, p) for n, ts, b in tokens) if t]
    return portfolio(trades, p)


def boot_ci(rets, iters=2000):
    rnd = random.Random(0)
    n = len(rets)
    means = sorted(statistics.fmean(rnd.choices(rets, k=n)) for _ in range(iters))
    return means[int(0.025 * iters)], means[int(0.975 * iters)]


def metrics(acc, n_tokens, p, skipped=0, ci=False):
    landed = [t for t in acc if t["reason"] != "failed"]
    out = {"tokens": n_tokens, "trades": len(landed),
           "failed_tx": len(acc) - len(landed), "skipped_busy": skipped}
    if not landed:
        out.update(win_rate=0, avg_ret_pct=0, total_pnl=0, return_on_capital_pct=0,
                   profit_factor=0, max_dd_pct_of_capital=0)
        return out
    pnls = [t["pnl"] for t in sorted(acc, key=lambda t: t["exit_ts"])]
    eq = peak = dd = 0.0
    for x in pnls:
        eq += x
        peak = max(peak, eq)
        dd = max(dd, peak - eq)
    gp = sum(x for x in pnls if x > 0)
    gl = -sum(x for x in pnls if x < 0)
    rets = [t["ret"] * 100 for t in landed]
    out.update(
        win_rate=round(100 * sum(t["pnl"] > 0 for t in landed) / len(landed), 1),
        avg_ret_pct=round(statistics.mean(rets), 2),
        median_ret_pct=round(statistics.median(rets), 2),
        total_pnl=round(sum(pnls), 2),
        return_on_capital_pct=round(100 * sum(pnls) / p.capital, 1),
        profit_factor=round(gp / gl, 2) if gl else float("inf"),
        max_dd_pct_of_capital=round(100 * dd / p.capital, 1),
        rug_or_honeypot=sum(t["reason"] in ("rug", "honeypot") for t in landed))
    if ci and len(rets) > 5:
        lo, hi = boot_ci(rets)
        out["avg_ret_95ci_pct"] = f"[{lo:.1f}, {hi:.1f}]"
    return out


def show(title, m):
    print(f"\n{title}")
    for k, v in m.items():
        print(f"  {k:22s} {v}")


def synth(n, seed, path, edge=0.0, minutes=120):
    """Synthetic launches. edge=0 is a no-edge world: early price action says
    nothing about what happens later, so a sane backtest should lose after
    costs. edge>0 makes strong early momentum raise the chance of a runner,
    to check the backtester CAN detect an edge when one exists."""
    rnd = random.Random(seed)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["token", "launch_ts", "t_min", "price", "high", "low", "liq"])
        for i in range(n):
            liq0 = math.exp(rnd.uniform(math.log(3000), math.log(60000)))
            rug_at = rnd.randint(10, 80)
            run_len = rnd.randint(15, 40)
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
                w.writerow([f"T{i}", i * 5, t, f"{px:.12g}", f"{hi:.12g}",
                            f"{lo:.12g}", f"{max(liq, 100):.2f}"])


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("synth")
    s.add_argument("--n", type=int, default=3000)
    s.add_argument("--seed", type=int, default=7)
    s.add_argument("--edge", type=float, default=0.0)
    s.add_argument("--out", default="synth.csv")
    for name in ("run", "sweep"):
        r = sub.add_parser(name)
        r.add_argument("--data", required=True)
        r.add_argument("--trades-out")
        if name == "run":
            for fld, v in P.__dataclass_fields__.items():
                r.add_argument(f"--{fld.replace('_', '-')}", type=type(v.default),
                               default=v.default)
    a = ap.parse_args()

    if a.cmd == "synth":
        synth(a.n, a.seed, a.out, a.edge)
        print(f"wrote {a.out}")
        return

    tokens = load(a.data)
    if a.cmd == "run":
        p = P(**{f: getattr(a, f) for f in P.__dataclass_fields__})
        acc, skipped = backtest(tokens, p)
        show("RESULTS", metrics(acc, len(tokens), p, skipped, ci=True))
        if a.trades_out and acc:
            with open(a.trades_out, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(acc[0].keys()))
                w.writeheader()
                w.writerows(acc)
            print(f"\nwrote {a.trades_out}")
        return

    # walk-forward: tune on first half (by launch time), report on second half
    half = len(tokens) // 2
    train, test = tokens[:half], tokens[half:]
    grid = list(itertools.product([0.05, 0.10, 0.20], [0.5, 1.0, 2.0],
                                  [0.2, 0.3, 0.5], [0, 1, 2]))
    base = P()
    best, best_pnl = None, -1e18
    for mom, tp, sl, lat in grid:
        p = replace(base, min_mom=mom, tp=tp, sl=sl, latency=lat)
        acc, _ = backtest(train, p)
        m = metrics(acc, len(train), p)
        if m["trades"] >= 30 and m["total_pnl"] > best_pnl:
            best, best_pnl = p, m["total_pnl"]
    if best is None:
        print("no parameter set produced enough trades")
        return
    acc, sk = backtest(train, best)
    show(f"BEST OF {len(grid)} ON TRAIN (in-sample)", metrics(acc, len(train), best, sk, ci=True))
    acc, sk = backtest(test, best)
    show("SAME PARAMS ON TEST (out-of-sample)", metrics(acc, len(test), best, sk, ci=True))
    print(f"\nchosen: min_mom={best.min_mom} tp={best.tp} sl={best.sl} latency={best.latency}")
    print("\nLATENCY SENSITIVITY (test half, chosen params)")
    for lat in (0, 1, 2, 3, 5):
        p = replace(best, latency=lat)
        acc, sk = backtest(test, p)
        m = metrics(acc, len(test), p, sk)
        print(f"  latency={lat}: trades={m['trades']} avg_ret={m['avg_ret_pct']}% pnl={m['total_pnl']}")


if __name__ == "__main__":
    main()
