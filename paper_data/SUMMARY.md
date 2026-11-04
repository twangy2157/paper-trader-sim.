# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T12:11:57Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 13. Pools on watchlist: 36.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 474 | 15% | -54.4% | -60 to -49 | -25830 |
| all momentum | 476 | 15% | -54.5% | -60 to -49 | -25970 |
| control | 563 | 7% | -17.6% | -20 to -15 | -9952 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 22 | 36% | -24.6% | -45 to -5 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (455, 16%) | -18% (563, 7%) | -13% (4, 25%) | -25% (22, 36%) |
| wide_sl50_tp100 | -55% (455, 17%) | -18% (563, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| sl30_tp50 | -57% (455, 19%) | -18% (563, 8%) | -22% (4, 25%) | -25% (22, 36%) |
| sl50_tp50 | -56% (455, 21%) | -18% (563, 9%) | -22% (4, 25%) | -25% (22, 36%) |
| no_stop_tp100 | -55% (455, 18%) | -18% (563, 8%) | -13% (4, 25%) | -25% (22, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 17345. Outcomes:

- missed_window: 11470
- low_liquidity: 3266
- proven_liquidity_gone: 1085
- no_momentum: 612
- research_failed: 479
- simulated failed buy: 192
- proven_low_volume: 166
- proven_price_collapsed_or_parabolic: 29
- proven: 25
- proven_no_uptrend: 15
- dip: 4
- research_passed: 2

Warning: 131 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
