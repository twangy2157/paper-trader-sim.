# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T11:16:20Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 33. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 463 | 15% | -54.3% | -60 to -48 | -25157 |
| all momentum | 465 | 15% | -54.3% | -60 to -49 | -25297 |
| control | 547 | 8% | -17.1% | -20 to -14 | -9423 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 22 | 36% | -24.6% | -45 to -5 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (444, 16%) | -17% (547, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| wide_sl50_tp100 | -55% (444, 17%) | -18% (547, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| sl30_tp50 | -57% (444, 19%) | -18% (547, 8%) | -22% (4, 25%) | -25% (22, 36%) |
| sl50_tp50 | -56% (444, 21%) | -18% (547, 9%) | -22% (4, 25%) | -25% (22, 36%) |
| no_stop_tp100 | -55% (444, 18%) | -18% (547, 8%) | -13% (4, 25%) | -25% (22, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 17111. Outcomes:

- missed_window: 11302
- low_liquidity: 3238
- proven_liquidity_gone: 1060
- no_momentum: 609
- research_failed: 475
- simulated failed buy: 191
- proven_low_volume: 163
- proven_price_collapsed_or_parabolic: 28
- proven: 25
- proven_no_uptrend: 14
- dip: 4
- research_passed: 2

Warning: 131 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
