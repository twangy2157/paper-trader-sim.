# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T14:41:41Z. Bankroll cash (research-selected trades): 898.0. Open positions: 25. Pools on watchlist: 32.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 315 | 14% | -54.4% | -62 to -47 | -17167 |
| all momentum | 316 | 14% | -54.6% | -61 to -48 | -17269 |
| control | 347 | 8% | -16.7% | -21 to -13 | -5841 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 14 | 36% | -32.3% | -61 to -5 | -453 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (295, 15%) | -17% (347, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| wide_sl50_tp100 | -55% (295, 17%) | -17% (347, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| sl30_tp50 | -57% (295, 19%) | -18% (347, 8%) | 7% (2, 50%) | -32% (14, 36%) |
| sl50_tp50 | -56% (295, 22%) | -18% (347, 9%) | 7% (2, 50%) | -32% (14, 36%) |
| no_stop_tp100 | -55% (295, 18%) | -17% (347, 8%) | 24% (2, 50%) | -32% (14, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11613. Outcomes:

- missed_window: 7677
- low_liquidity: 2384
- proven_liquidity_gone: 566
- no_momentum: 406
- research_failed: 324
- simulated failed buy: 118
- proven_low_volume: 96
- proven: 15
- proven_price_collapsed_or_parabolic: 15
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 75 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
