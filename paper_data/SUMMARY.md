# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T14:10:54Z. Bankroll cash (research-selected trades): 898.0. Open positions: 24. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 310 | 14% | -54.8% | -62 to -48 | -17023 |
| all momentum | 311 | 14% | -55.0% | -62 to -48 | -17125 |
| control | 344 | 8% | -16.8% | -21 to -13 | -5820 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 13 | 38% | -34.3% | -66 to -6 | -446 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (290, 15%) | -17% (344, 8%) | 24% (2, 50%) | -34% (13, 38%) |
| wide_sl50_tp100 | -56% (290, 17%) | -17% (344, 8%) | 24% (2, 50%) | -34% (13, 38%) |
| sl30_tp50 | -57% (290, 19%) | -18% (344, 8%) | 7% (2, 50%) | -34% (13, 38%) |
| sl50_tp50 | -56% (290, 22%) | -18% (344, 9%) | 7% (2, 50%) | -34% (13, 38%) |
| no_stop_tp100 | -56% (290, 17%) | -17% (344, 8%) | 24% (2, 50%) | -34% (13, 38%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11427. Outcomes:

- missed_window: 7546
- low_liquidity: 2360
- proven_liquidity_gone: 550
- no_momentum: 397
- research_failed: 323
- simulated failed buy: 116
- proven_low_volume: 93
- proven: 15
- proven_price_collapsed_or_parabolic: 15
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 74 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
