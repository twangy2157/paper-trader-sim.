# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T07:13:09Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 14. Pools on watchlist: 39.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 944 | 13% | -60.3% | -64 to -56 | -56989 |
| all momentum | 956 | 13% | -59.9% | -64 to -56 | -57384 |
| control | 1202 | 6% | -20.0% | -22 to -18 | -24137 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 47 | 47% | -14.4% | -29 to -1 | -682 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (935, 14%) | -20% (1202, 6%) | -40% (10, 10%) | -14% (47, 47%) |
| wide_sl50_tp100 | -60% (935, 15%) | -20% (1202, 7%) | -43% (10, 10%) | -14% (47, 47%) |
| sl30_tp50 | -62% (935, 16%) | -20% (1202, 7%) | -44% (10, 10%) | -17% (47, 47%) |
| sl50_tp50 | -61% (935, 18%) | -21% (1202, 8%) | -47% (10, 10%) | -17% (47, 47%) |
| no_stop_tp100 | -60% (935, 16%) | -21% (1202, 7%) | -40% (10, 10%) | -14% (47, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 33589. Outcomes:

- missed_window: 21791
- low_liquidity: 6081
- proven_liquidity_gone: 2577
- no_momentum: 1253
- research_failed: 950
- simulated failed buy: 415
- proven_low_volume: 371
- proven_price_collapsed_or_parabolic: 58
- proven: 48
- proven_no_uptrend: 23
- research_passed: 12
- dip: 10

Warning: 265 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
