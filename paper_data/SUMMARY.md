# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T15:32:44Z. Bankroll cash (research-selected trades): 798.0. Open positions: 25. Pools on watchlist: 67.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 324 | 14% | -54.6% | -61 to -48 | -17727 |
| all momentum | 325 | 14% | -54.8% | -62 to -48 | -17829 |
| control | 358 | 8% | -16.3% | -20 to -13 | -5851 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 14 | 36% | -32.3% | -61 to -5 | -453 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (304, 15%) | -16% (358, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| wide_sl50_tp100 | -56% (304, 17%) | -17% (358, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| sl30_tp50 | -57% (304, 19%) | -18% (358, 8%) | 7% (2, 50%) | -32% (14, 36%) |
| sl50_tp50 | -56% (304, 22%) | -17% (358, 9%) | 7% (2, 50%) | -32% (14, 36%) |
| no_stop_tp100 | -55% (304, 17%) | -17% (358, 8%) | 24% (2, 50%) | -32% (14, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11852. Outcomes:

- missed_window: 7841
- low_liquidity: 2416
- proven_liquidity_gone: 585
- no_momentum: 416
- research_failed: 333
- simulated failed buy: 121
- proven_low_volume: 97
- proven: 15
- proven_price_collapsed_or_parabolic: 15
- proven_no_uptrend: 9
- research_passed: 2
- dip: 2

Warning: 78 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
