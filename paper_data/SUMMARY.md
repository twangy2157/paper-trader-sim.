# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T02:28:34Z. Bankroll cash (research-selected trades): 898.5. Open positions: 26. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 214 | 15% | -51.8% | -60 to -43 | -11100 |
| all momentum | 215 | 15% | -52.0% | -60 to -44 | -11201 |
| control | 234 | 9% | -16.5% | -21 to -11 | -3874 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 3 | 0% | -100.0% | - | -300 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (194, 16%) | -16% (234, 9%) | - | -100% (3, 0%) |
| wide_sl50_tp100 | -54% (194, 17%) | -17% (234, 9%) | - | -100% (3, 0%) |
| sl30_tp50 | -55% (194, 20%) | -18% (234, 9%) | - | -100% (3, 0%) |
| sl50_tp50 | -55% (194, 22%) | -18% (234, 9%) | - | -100% (3, 0%) |
| no_stop_tp100 | -54% (194, 18%) | -17% (234, 9%) | - | -100% (3, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8464. Outcomes:

- missed_window: 5611
- low_liquidity: 1904
- no_momentum: 294
- proven_liquidity_gone: 272
- research_failed: 223
- simulated failed buy: 84
- proven_low_volume: 56
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1

Warning: 57 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
