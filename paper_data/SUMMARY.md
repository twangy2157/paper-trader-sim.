# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T11:38:45Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 33. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 466 | 15% | -54.4% | -60 to -49 | -25398 |
| all momentum | 468 | 15% | -54.5% | -60 to -49 | -25538 |
| control | 550 | 8% | -17.2% | -20 to -14 | -9535 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 22 | 36% | -24.6% | -45 to -5 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (447, 16%) | -17% (550, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| wide_sl50_tp100 | -55% (447, 17%) | -18% (550, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| sl30_tp50 | -57% (447, 19%) | -18% (550, 8%) | -22% (4, 25%) | -25% (22, 36%) |
| sl50_tp50 | -56% (447, 21%) | -18% (550, 9%) | -22% (4, 25%) | -25% (22, 36%) |
| no_stop_tp100 | -55% (447, 18%) | -18% (550, 8%) | -13% (4, 25%) | -25% (22, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 17203. Outcomes:

- missed_window: 11359
- low_liquidity: 3253
- proven_liquidity_gone: 1071
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
