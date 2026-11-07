# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T11:38:29Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 21. Pools on watchlist: 39.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 974 | 13% | -60.8% | -64 to -57 | -59319 |
| all momentum | 986 | 13% | -60.5% | -64 to -57 | -59714 |
| control | 1253 | 6% | -20.0% | -22 to -18 | -25234 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 51 | 47% | -16.7% | -30 to -3 | -857 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (965, 13%) | -20% (1253, 6%) | -40% (10, 10%) | -17% (51, 47%) |
| wide_sl50_tp100 | -61% (965, 15%) | -20% (1253, 7%) | -43% (10, 10%) | -17% (51, 47%) |
| sl30_tp50 | -62% (965, 16%) | -20% (1253, 7%) | -44% (10, 10%) | -19% (51, 47%) |
| sl50_tp50 | -62% (965, 18%) | -21% (1253, 8%) | -47% (10, 10%) | -19% (51, 47%) |
| no_stop_tp100 | -60% (965, 16%) | -21% (1253, 7%) | -40% (10, 10%) | -17% (51, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 34682. Outcomes:

- missed_window: 22451
- low_liquidity: 6278
- proven_liquidity_gone: 2690
- no_momentum: 1306
- research_failed: 985
- simulated failed buy: 432
- proven_low_volume: 385
- proven_price_collapsed_or_parabolic: 58
- proven: 52
- proven_no_uptrend: 23
- research_passed: 12
- dip: 10

Warning: 270 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
