# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T05:41:00Z. Bankroll cash (research-selected trades): 898.0. Open positions: 24. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 239 | 15% | -51.7% | -60 to -44 | -12371 |
| all momentum | 240 | 15% | -51.9% | -60 to -44 | -12473 |
| control | 266 | 9% | -16.5% | -21 to -12 | -4423 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (219, 16%) | -17% (266, 9%) | 58% (1, 100%) | -100% (4, 0%) |
| wide_sl50_tp100 | -54% (219, 17%) | -17% (266, 9%) | 58% (1, 100%) | -100% (4, 0%) |
| sl30_tp50 | -55% (219, 19%) | -18% (266, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| sl50_tp50 | -55% (219, 21%) | -18% (266, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| no_stop_tp100 | -54% (219, 17%) | -17% (266, 9%) | 58% (1, 100%) | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9362. Outcomes:

- missed_window: 6200
- low_liquidity: 2061
- proven_liquidity_gone: 349
- no_momentum: 323
- research_failed: 248
- simulated failed buy: 93
- proven_low_volume: 63
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 8
- proven: 6
- research_passed: 1
- dip: 1

Warning: 61 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
