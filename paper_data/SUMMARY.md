# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T15:20:54Z. Bankroll cash (research-selected trades): 505.1869477321155. Open positions: 23. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 1006 | 13% | -61.2% | -65 to -57 | -61625 |
| all momentum | 1018 | 13% | -60.8% | -64 to -57 | -62020 |
| control | 1284 | 6% | -20.0% | -22 to -18 | -25849 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 52 | 48% | -15.9% | -30 to -3 | -832 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (997, 13%) | -20% (1284, 6%) | -40% (10, 10%) | -16% (52, 48%) |
| wide_sl50_tp100 | -61% (997, 15%) | -20% (1284, 7%) | -43% (10, 10%) | -16% (52, 48%) |
| sl30_tp50 | -62% (997, 16%) | -20% (1284, 7%) | -44% (10, 10%) | -18% (52, 48%) |
| sl50_tp50 | -62% (997, 18%) | -21% (1284, 7%) | -47% (10, 10%) | -18% (52, 48%) |
| no_stop_tp100 | -61% (997, 16%) | -21% (1284, 7%) | -40% (10, 10%) | -16% (52, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 35653. Outcomes:

- missed_window: 23078
- low_liquidity: 6441
- proven_liquidity_gone: 2786
- no_momentum: 1340
- research_failed: 1015
- simulated failed buy: 441
- proven_low_volume: 394
- proven_price_collapsed_or_parabolic: 58
- proven: 53
- proven_no_uptrend: 24
- research_passed: 13
- dip: 10

Warning: 278 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
