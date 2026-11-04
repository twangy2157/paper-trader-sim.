# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T12:32:38Z. Bankroll cash (research-selected trades): 859.5946161788225. Open positions: 15. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 477 | 15% | -54.3% | -60 to -49 | -25938 |
| all momentum | 479 | 15% | -54.4% | -60 to -49 | -26078 |
| control | 566 | 7% | -17.5% | -20 to -15 | -9971 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 22 | 36% | -24.6% | -45 to -5 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (458, 16%) | -18% (566, 7%) | -13% (4, 25%) | -25% (22, 36%) |
| wide_sl50_tp100 | -55% (458, 17%) | -18% (566, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| sl30_tp50 | -57% (458, 19%) | -18% (566, 8%) | -22% (4, 25%) | -25% (22, 36%) |
| sl50_tp50 | -56% (458, 21%) | -18% (566, 9%) | -22% (4, 25%) | -25% (22, 36%) |
| no_stop_tp100 | -54% (458, 18%) | -18% (566, 8%) | -13% (4, 25%) | -25% (22, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 17434. Outcomes:

- missed_window: 11525
- low_liquidity: 3278
- proven_liquidity_gone: 1095
- no_momentum: 618
- research_failed: 480
- simulated failed buy: 194
- proven_low_volume: 166
- proven_price_collapsed_or_parabolic: 31
- proven: 26
- proven_no_uptrend: 15
- dip: 4
- research_passed: 2

Warning: 131 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
