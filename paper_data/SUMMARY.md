# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T14:17:20Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 23. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 997 | 13% | -61.2% | -65 to -57 | -61119 |
| all momentum | 1009 | 13% | -60.9% | -64 to -57 | -61514 |
| control | 1271 | 6% | -20.0% | -22 to -18 | -25595 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 52 | 48% | -15.9% | -30 to -3 | -832 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (988, 13%) | -20% (1271, 6%) | -40% (10, 10%) | -16% (52, 48%) |
| wide_sl50_tp100 | -61% (988, 15%) | -20% (1271, 7%) | -43% (10, 10%) | -16% (52, 48%) |
| sl30_tp50 | -63% (988, 16%) | -20% (1271, 7%) | -44% (10, 10%) | -18% (52, 48%) |
| sl50_tp50 | -62% (988, 18%) | -21% (1271, 7%) | -47% (10, 10%) | -18% (52, 48%) |
| no_stop_tp100 | -61% (988, 16%) | -21% (1271, 7%) | -40% (10, 10%) | -16% (52, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 35346. Outcomes:

- missed_window: 22867
- low_liquidity: 6401
- proven_liquidity_gone: 2761
- no_momentum: 1328
- research_failed: 1006
- simulated failed buy: 435
- proven_low_volume: 391
- proven_price_collapsed_or_parabolic: 58
- proven: 53
- proven_no_uptrend: 24
- research_passed: 12
- dip: 10

Warning: 273 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
