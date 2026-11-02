#!/usr/bin/env python3
"""Backtest three simple rules on ESTABLISHED memecoins (hourly bars). Paper only.

It downloads public hourly candles from Binance's market-data endpoint (no key,
no account), runs three rules with FIXED parameters (nothing is tuned), charges
fees and slippage, and writes backtest_data/RESULTS.md.

  python backtest_established.py --out backtest_data
  python backtest_established.py --synthetic        # offline self-test, fake data

Rules (long only, one position per coin at a time, signal at bar close, fill at
the NEXT bar's open):
  momentum : close breaks the 72h high AND is above the 200h average.
             exit: 12% trailing stop from the high, or 14 days.
  dip      : price is 15% below its 72h high AND RSI(14) < 30.
             exit: +8% target, -8% stop (stop wins ties), or 48h.
  trend    : 24h average crosses above the 168h average; exit when it crosses back.
Costs: 0.10% fee per side + 0.05% slippage per side (0.30% round trip).

Read the results with care:
  * Memecoins move together, so trades across coins are NOT independent and the
    confidence intervals are too narrow.
  * Three rules x six coins x two periods = many looks. One lucky cell is expected.
  * 'Out-of-sample' = the last 40% of each coin's history, never used to pick rules,
    but I did choose the rules after seeing that new-pool sniping lost.
"""
import argparse
import csv
import json
import os
import random
import statistics
import time
import urllib.request
from datetime import datetime, timezone

COINS = ["DOGEUSDT", "SHIBUSDT", "PEPEUSDT", "BONKUSDT", "WIFUSDT", "FLOKIUSDT"]
BASE = "https://data-api.binance.vision/api/v3/klines"
FEE, SLIP = 0.001, 0.0005
H = 3600 * 1000


# ---------------- data ----------------
def fetch(symbol, start_ms, cache):
    if os.path.exists(cache):
        with open(cache) as f:
            return [[float(x) for x in r] for r in list(csv.reader(f))[1:]]
    rows, t = [], start_ms
    while True:
        url = f"{BASE}?symbol={symbol}&interval=1h&startTime={t}&limit=1000"
        with urllib.request.urlopen(urllib.request.Request(
                url, headers={"User-Agent": "paper-backtest/1.0"}), timeout=30) as r:
            chunk = json.load(r)
        if not chunk:
            break
        rows += [[c[0], c[1], c[2], c[3], c[4], c[5]] for c in chunk]
        t = chunk[-1][0] + H
        if len(chunk) < 1000:
            break
        time.sleep(0.25)
    with open(cache, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["t", "o", "h", "l", "c", "v"])
        w.writerows(rows)
    return [[float(x) for x in r] for r in rows]


def synthetic(seed, n=24000, edge=0.0, t0=1672531200000):
    rnd = random.Random(seed)
    p, rows, t = 1.0, [], t0
    for _ in range(n):
        r = rnd.gauss(edge, 0.012) * (3 if rnd.random() < 0.02 else 1)
        o = p
        p = max(1e-6, p * (1 + r))
        hi = max(o, p) * (1 + abs(rnd.gauss(0, 0.004)))
        lo = min(o, p) * (1 - abs(rnd.gauss(0, 0.004)))
        rows.append([t, o, hi, lo, p, 1000.0])
        t += H
    return rows


# ---------------- indicators ----------------
def sma(x, n):
    out, s = [None] * len(x), 0.0
    for i, v in enumerate(x):
        s += v
        if i >= n:
            s -= x[i - n]
        if i >= n - 1:
            out[i] = s / n
    return out


def rsi(c, n=14):
    out = [None] * len(c)
    if len(c) <= n:
        return out
    g = [max(c[i] - c[i - 1], 0) for i in range(1, len(c))]
    l = [max(c[i - 1] - c[i], 0) for i in range(1, len(c))]
    ag, al = sum(g[:n]) / n, sum(l[:n]) / n
    for i in range(n, len(c)):
        if i > n:
            ag = (ag * (n - 1) + g[i - 1]) / n
            al = (al * (n - 1) + l[i - 1]) / n
        out[i] = 100 if al == 0 else 100 - 100 / (1 + ag / al)
    return out


# ---------------- trades ----------------
def net_ret(entry_open, exit_px):
    buy = entry_open * (1 + SLIP) * (1 + FEE)
    sell = exit_px * (1 - SLIP) * (1 - FEE)
    return sell / buy - 1


def run(rows, rule, open_out=None):
    t = [r[0] for r in rows]
    o, h, l, c = ([r[k] for r in rows] for k in (1, 2, 3, 4))
    n = len(rows)
    ma200, ma24, ma168, rs = sma(c, 200), sma(c, 24), sma(c, 168), rsi(c)
    trades, i = [], 200
    while i < n - 2:
        enter = False
        if rule == "momentum":
            enter = c[i] > max(h[i - 72:i]) and ma200[i] is not None and c[i] > ma200[i]
        elif rule == "dip":
            enter = c[i] <= 0.85 * max(h[i - 72:i]) and rs[i] is not None and rs[i] < 30
        elif rule == "trend":
            enter = (ma24[i] is not None and ma168[i] is not None and ma24[i] > ma168[i]
                     and ma24[i - 1] is not None and ma168[i - 1] is not None
                     and ma24[i - 1] <= ma168[i - 1])
        if not enter:
            i += 1
            continue
        e = i + 1
        entry = o[e]
        j, exit_px, hw = e, None, entry
        while j < n:
            if rule == "momentum":
                stop = hw * 0.88
                if l[j] <= stop and j > e:
                    exit_px = min(o[j], stop)
                    break
                hw = max(hw, h[j])
                if j - e >= 336:
                    exit_px = c[j]
                    break
            elif rule == "dip":
                if l[j] <= entry * 0.92:                  # stop wins ties
                    exit_px = min(o[j], entry * 0.92)
                    break
                if h[j] >= entry * 1.08:
                    exit_px = entry * 1.08
                    break
                if j - e >= 48:
                    exit_px = c[j]
                    break
            else:
                if ma24[j] is not None and ma168[j] is not None and ma24[j] < ma168[j]:
                    exit_px = c[j]
                    break
            j += 1
        if exit_px is None:                                  # still open at the end of the data
            if open_out is not None:
                open_out.append({"t": t[e], "entry": entry, "last": c[-1],
                                 "ret": net_ret(entry, c[-1])})
            break
        trades.append((t[e], net_ret(entry, exit_px)))
        i = max(j, i + 1)
    return trades


def boot_ci(xs, k=2000, seed=1):
    rnd = random.Random(seed)
    m = sorted(statistics.mean(rnd.choices(xs, k=len(xs))) for _ in range(k))
    return m[int(0.025 * k)], m[int(0.975 * k)]


def stats(rets):
    if not rets:
        return "0 | - | - | -"
    ci = "-"
    if len(rets) >= 20:
        lo, hi = boot_ci(rets)
        ci = f"{100 * lo:.2f} to {100 * hi:.2f}"
    return (f"{len(rets)} | {100 * sum(r > 0 for r in rets) / len(rets):.0f}% | "
            f"{100 * statistics.mean(rets):.2f}% | {ci}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="backtest_data")
    ap.add_argument("--start", default="2023-01-01")
    ap.add_argument("--synthetic", action="store_true")
    ap.add_argument("--edge", type=float, default=0.0, help="synthetic drift per hour")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    start_ms = int(datetime.fromisoformat(a.start).replace(tzinfo=timezone.utc).timestamp() * 1000)

    data = {}
    for k, sym in enumerate(COINS):
        try:
            data[sym] = (synthetic(k, edge=a.edge) if a.synthetic else
                         fetch(sym, start_ms, os.path.join(a.out, f"{sym}_1h.csv")))
        except Exception as e:
            print("could not load", sym, e)
    if not data:
        raise SystemExit("no data loaded")

    rules = ["momentum", "dip", "trend"]
    allr = {r: {"is": [], "oos": []} for r in rules}
    percoin = []
    for sym, rows in data.items():
        cut = rows[int(len(rows) * 0.6)][0]
        c0, c1 = rows[0][4], rows[-1][4]
        o0 = rows[int(len(rows) * 0.6)][4]
        bh_all = net_ret(rows[1][1], c1)
        bh_oos = net_ret(o0, c1)
        row = {"sym": sym, "bars": len(rows), "bh_all": bh_all, "bh_oos": bh_oos}
        for r in rules:
            tr = run(rows, r)
            ins = [x for tt, x in tr if tt < cut]
            oos = [x for tt, x in tr if tt >= cut]
            allr[r]["is"] += ins
            allr[r]["oos"] += oos
            comp = lambda xs: (lambda p: p - 1)(__import__("math").prod(1 + x for x in xs))
            row[r] = (len(oos), comp(oos))
        percoin.append(row)

    L = ["# Established memecoin backtest", "",
         "SIMULATION ONLY. Hourly bars, fixed rules, 0.30% round-trip costs.",
         f"Updated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%MZ')}. "
         f"Coins loaded: {', '.join(s.replace('USDT', '') for s in data)}.", "",
         "## All coins pooled (return per trade, after costs)", "",
         "| rule | period | trades | win | avg | 95% CI of avg % |", "|---|---|---|---|---|---|"]
    for r in rules:
        for per, lab in (("is", "first 60%"), ("oos", "last 40%")):
            L.append(f"| {r} | {lab} | {stats(allr[r][per])} |")
    L += ["", "## Last 40% of each coin: total return, compounding every trade",
          "", "| coin | buy & hold | momentum | dip | trend |", "|---|---|---|---|---|"]
    for row in percoin:
        cells = " | ".join(f"{100 * row[r][1]:.0f}% ({row[r][0]})" for r in rules)
        L.append(f"| {row['sym'].replace('USDT', '')} | {100 * row['bh_oos']:.0f}% | {cells} |")
    L += ["", "Cells show total return (number of trades). Buy & hold is the benchmark: a rule",
          "that earns less than holding the coin, with similar risk, adds nothing.", "",
          "## How to read this", "",
          "- A rule is only interesting if the last-40% CI lower bound is above 0 AND it also",
          "  looked decent in the first 60%. Anything else is noise or luck.",
          "- CIs here are too narrow: coins move together, so trades are not independent.",
          "- Memecoins mostly fell over long stretches, so 'buy and hold' can be very negative;",
          "  beating it by losing less is not the same as making money."]
    with open(os.path.join(a.out, "RESULTS.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
