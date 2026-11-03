# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T14:51:57Z. Bankroll cash (research-selected trades): 898.0. Open positions: 23. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 319 | 14% | -54.2% | -61 to -47 | -17317 |
| all momentum | 320 | 14% | -54.3% | -61 to -47 | -17419 |
| control | 348 | 8% | -16.7% | -21 to -13 | -5849 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 14 | 36% | -32.3% | -61 to -5 | -453 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (299, 15%) | -17% (348, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| wide_sl50_tp100 | -55% (299, 17%) | -17% (348, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| sl30_tp50 | -57% (299, 19%) | -18% (348, 8%) | 7% (2, 50%) | -32% (14, 36%) |
| sl50_tp50 | -56% (299, 22%) | -18% (348, 9%) | 7% (2, 50%) | -32% (14, 36%) |
| no_stop_tp100 | -55% (299, 18%) | -17% (348, 8%) | 24% (2, 50%) | -32% (14, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11650. Outcomes:

- missed_window: 7702
- low_liquidity: 2390
- proven_liquidity_gone: 568
- no_momentum: 407
- research_failed: 326
- simulated failed buy: 119
- proven_low_volume: 96
- proven: 15
- proven_price_collapsed_or_parabolic: 15
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 76 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
