# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T09:30:39Z. Bankroll cash (research-selected trades): 898.0. Open positions: 31. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 271 | 15% | -52.0% | -59 to -44 | -14122 |
| all momentum | 272 | 15% | -52.2% | -60 to -44 | -14224 |
| control | 299 | 9% | -16.2% | -20 to -12 | -4881 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 7 | 29% | -56.9% | -87 to -14 | -399 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (251, 16%) | -16% (299, 9%) | 58% (1, 100%) | -57% (7, 29%) |
| wide_sl50_tp100 | -54% (251, 18%) | -17% (299, 9%) | 58% (1, 100%) | -57% (7, 29%) |
| sl30_tp50 | -55% (251, 21%) | -18% (299, 9%) | 24% (1, 100%) | -57% (7, 29%) |
| sl50_tp50 | -54% (251, 23%) | -17% (299, 10%) | 24% (1, 100%) | -57% (7, 29%) |
| no_stop_tp100 | -54% (251, 18%) | -17% (299, 9%) | 58% (1, 100%) | -57% (7, 29%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10250. Outcomes:

- missed_window: 6771
- low_liquidity: 2187
- proven_liquidity_gone: 437
- no_momentum: 359
- research_failed: 282
- simulated failed buy: 105
- proven_low_volume: 74
- proven_price_collapsed_or_parabolic: 13
- proven: 11
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 69 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
