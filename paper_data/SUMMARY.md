# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T09:09:10Z. Bankroll cash (research-selected trades): 898.0. Open positions: 34. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 266 | 15% | -51.8% | -59 to -44 | -13791 |
| all momentum | 267 | 15% | -51.9% | -59 to -44 | -13893 |
| control | 295 | 9% | -16.0% | -21 to -12 | -4758 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 6 | 33% | -65.7% | -100 to -31 | -395 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (246, 16%) | -16% (295, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| wide_sl50_tp100 | -54% (246, 17%) | -17% (295, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| sl30_tp50 | -55% (246, 21%) | -17% (295, 9%) | 24% (1, 100%) | -66% (6, 33%) |
| sl50_tp50 | -54% (246, 23%) | -17% (295, 10%) | 24% (1, 100%) | -66% (6, 33%) |
| no_stop_tp100 | -54% (246, 18%) | -16% (295, 9%) | 58% (1, 100%) | -66% (6, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10136. Outcomes:

- missed_window: 6689
- low_liquidity: 2175
- proven_liquidity_gone: 426
- no_momentum: 353
- research_failed: 281
- simulated failed buy: 104
- proven_low_volume: 73
- proven_price_collapsed_or_parabolic: 13
- proven: 11
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 68 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
