# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T12:00:10Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 21. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 469 | 15% | -54.4% | -60 to -48 | -25536 |
| all momentum | 471 | 15% | -54.4% | -60 to -49 | -25676 |
| control | 560 | 8% | -17.3% | -20 to -14 | -9741 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 22 | 36% | -24.6% | -45 to -5 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (450, 16%) | -17% (560, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| wide_sl50_tp100 | -55% (450, 17%) | -18% (560, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| sl30_tp50 | -57% (450, 19%) | -18% (560, 8%) | -22% (4, 25%) | -25% (22, 36%) |
| sl50_tp50 | -56% (450, 21%) | -18% (560, 9%) | -22% (4, 25%) | -25% (22, 36%) |
| no_stop_tp100 | -54% (450, 18%) | -18% (560, 8%) | -13% (4, 25%) | -25% (22, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 17305. Outcomes:

- missed_window: 11442
- low_liquidity: 3261
- proven_liquidity_gone: 1079
- no_momentum: 612
- research_failed: 479
- simulated failed buy: 192
- proven_low_volume: 165
- proven_price_collapsed_or_parabolic: 29
- proven: 25
- proven_no_uptrend: 15
- dip: 4
- research_passed: 2

Warning: 131 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
