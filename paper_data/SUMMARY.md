# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T15:22:36Z. Bankroll cash (research-selected trades): 898.0. Open positions: 23. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 323 | 14% | -54.5% | -61 to -48 | -17627 |
| all momentum | 324 | 14% | -54.6% | -61 to -48 | -17729 |
| control | 355 | 8% | -16.3% | -20 to -12 | -5830 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 14 | 36% | -32.3% | -61 to -5 | -453 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (303, 15%) | -16% (355, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| wide_sl50_tp100 | -56% (303, 17%) | -17% (355, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| sl30_tp50 | -57% (303, 19%) | -18% (355, 8%) | 7% (2, 50%) | -32% (14, 36%) |
| sl50_tp50 | -56% (303, 22%) | -18% (355, 9%) | 7% (2, 50%) | -32% (14, 36%) |
| no_stop_tp100 | -55% (303, 17%) | -17% (355, 8%) | 24% (2, 50%) | -32% (14, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11803. Outcomes:

- missed_window: 7808
- low_liquidity: 2410
- proven_liquidity_gone: 581
- no_momentum: 412
- research_failed: 332
- simulated failed buy: 121
- proven_low_volume: 97
- proven: 15
- proven_price_collapsed_or_parabolic: 15
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 78 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
