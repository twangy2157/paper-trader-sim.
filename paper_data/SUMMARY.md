# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T14:21:10Z. Bankroll cash (research-selected trades): 898.0. Open positions: 21. Pools on watchlist: 79.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 314 | 14% | -54.6% | -62 to -47 | -17161 |
| all momentum | 315 | 14% | -54.7% | -61 to -48 | -17263 |
| control | 344 | 8% | -16.8% | -21 to -13 | -5820 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 14 | 36% | -32.3% | -61 to -5 | -453 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (294, 15%) | -17% (344, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| wide_sl50_tp100 | -56% (294, 17%) | -17% (344, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| sl30_tp50 | -57% (294, 19%) | -18% (344, 8%) | 7% (2, 50%) | -32% (14, 36%) |
| sl50_tp50 | -56% (294, 22%) | -18% (344, 9%) | 7% (2, 50%) | -32% (14, 36%) |
| no_stop_tp100 | -55% (294, 18%) | -17% (344, 8%) | 24% (2, 50%) | -32% (14, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11473. Outcomes:

- missed_window: 7577
- low_liquidity: 2367
- proven_liquidity_gone: 556
- no_momentum: 399
- research_failed: 323
- simulated failed buy: 116
- proven_low_volume: 93
- proven: 15
- proven_price_collapsed_or_parabolic: 15
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 74 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
