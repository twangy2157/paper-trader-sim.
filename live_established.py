#!/usr/bin/env python3
"""LIVE paper trading of the established-memecoin rules. Simulation only.

Every hour it downloads the last ~40 days of hourly candles, re-runs the exact
rules from backtest_established.py, and reports only the trades that STARTED
after the go-live time (saved in live_data/golive.txt the first time it runs).
It is stateless: no ledger to corrupt, the same data always gives the same answer.
Trades that opened before go-live are ignored, but one that was still open at
go-live can block the first entry slightly. Nothing here places any order.

  python live_established.py --out live_data
  python live_established.py --synthetic --out /tmp/live_test   # offline self-test
"""
import argparse
import csv
import json
import os
import statistics
import time
import urllib.request
from datetime import datetime, timezone

import backtest_established as be

H = be.H


def fetch_recent(symbol, days=40):
    start = int((time.time() - days * 86400) * 1000)
    url = f"{be.BASE}?symbol={symbol}&interval=1h&startTime={start}&limit=1000"
    with urllib.request.urlopen(urllib.request.Request(
            url, headers={"User-Agent": "paper-live/1.0"}), timeout=30) as r:
        chunk = json.load(r)
    rows = [[float(x) for x in (c[0], c[1], c[2], c[3], c[4], c[5])] for c in chunk]
    if rows and rows[-1][0] + H > time.time() * 1000:        # drop the still-forming hour
        rows = rows[:-1]
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="live_data")
    ap.add_argument("--synthetic", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    now_ms = int(time.time() * 1000)
    now_h = now_ms - now_ms % H

    gl_path = os.path.join(a.out, "golive.txt")
    if os.path.exists(gl_path):
        golive = int(open(gl_path).read().strip())
    else:
        golive = now_h - (14 * 24 * H if a.synthetic else 0)
        open(gl_path, "w").write(str(golive))

    rules = ["momentum", "dip", "trend"]
    closed, opened, errors = [], [], []
    for k, sym in enumerate(be.COINS):
        try:
            rows = (be.synthetic(k, n=960, edge=0.0, t0=now_h - 960 * H) if a.synthetic
                    else fetch_recent(sym))
        except Exception as e:
            errors.append(f"{sym}: {e}")
            continue
        coin = sym.replace("USDT", "")
        for r in rules:
            op = []
            for tt, x in be.run(rows, r, open_out=op):
                if tt >= golive:
                    closed.append((coin, r, tt, x))
            for o in op:
                if o["t"] >= golive:
                    opened.append((coin, r, o))
        time.sleep(0.3)

    with open(os.path.join(a.out, "trades.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["coin", "rule", "entry_time_utc", "return_pct_after_costs"])
        for coin, r, tt, x in sorted(closed, key=lambda z: z[2]):
            w.writerow([coin, r, datetime.fromtimestamp(tt / 1000, timezone.utc)
                        .strftime("%Y-%m-%d %H:%M"), round(100 * x, 2)])

    ts = lambda ms: datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%Y-%m-%d %H:%M")
    L = ["# Live paper trading: established memecoins", "",
         "SIMULATION ONLY. Fixed rules, 0.30% round-trip costs, hourly bars.", "",
         f"Live since {ts(golive)} UTC. Updated {ts(now_h)} UTC.", "",
         "| rule | closed | win | avg | open now |", "|---|---|---|---|---|"]
    for r in rules:
        xs = [x for _c, rr, _t, x in closed if rr == r]
        n_open = sum(1 for _c, rr, _o in opened if rr == r)
        if xs:
            L.append(f"| {r} | {len(xs)} | {100 * sum(v > 0 for v in xs) / len(xs):.0f}% | "
                     f"{100 * statistics.mean(xs):.2f}% | {n_open} |")
        else:
            L.append(f"| {r} | 0 | - | - | {n_open} |")
    if opened:
        L += ["", "Open positions (marked at the last closed hour):", "",
              "| coin | rule | opened | return so far |", "|---|---|---|---|"]
        for coin, r, o in sorted(opened, key=lambda z: z[2]["t"]):
            L.append(f"| {coin} | {r} | {ts(o['t'])} | {100 * o['ret']:.1f}% |")
    L += ["", "Each rule needs 30+ closed trades before the average means anything,",
          "and the coins move together, so treat any early result as noise."]
    if errors:
        L += ["", "Data errors this run: " + "; ".join(errors)]
    with open(os.path.join(a.out, "LIVE.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
