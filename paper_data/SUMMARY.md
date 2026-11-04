# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T11:50:00Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 27. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 468 | 15% | -54.4% | -60 to -48 | -25503 |
| all momentum | 470 | 15% | -54.5% | -60 to -49 | -25643 |
| control | 554 | 8% | -17.2% | -20 to -14 | -9598 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 22 | 36% | -24.6% | -45 to -5 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (449, 16%) | -17% (554, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| wide_sl50_tp100 | -55% (449, 17%) | -18% (554, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| sl30_tp50 | -57% (449, 19%) | -18% (554, 8%) | -22% (4, 25%) | -25% (22, 36%) |
| sl50_tp50 | -56% (449, 21%) | -18% (554, 9%) | -22% (4, 25%) | -25% (22, 36%) |
| no_stop_tp100 | -55% (449, 18%) | -18% (554, 8%) | -13% (4, 25%) | -25% (22, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 17256. Outcomes:

- missed_window: 11400
- low_liquidity: 3260
- proven_liquidity_gone: 1076
- no_momentum: 612
- research_failed: 478
- simulated failed buy: 192
- proven_low_volume: 164
- proven_price_collapsed_or_parabolic: 29
- proven: 25
- proven_no_uptrend: 14
- dip: 4
- research_passed: 2

Warning: 131 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
