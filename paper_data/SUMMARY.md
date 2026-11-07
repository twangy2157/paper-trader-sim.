# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T14:37:40Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 19. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 1000 | 13% | -61.1% | -65 to -57 | -61239 |
| all momentum | 1012 | 13% | -60.8% | -64 to -57 | -61634 |
| control | 1277 | 6% | -20.1% | -22 to -18 | -25741 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 52 | 48% | -15.9% | -30 to -3 | -832 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (991, 13%) | -20% (1277, 6%) | -40% (10, 10%) | -16% (52, 48%) |
| wide_sl50_tp100 | -61% (991, 15%) | -21% (1277, 7%) | -43% (10, 10%) | -16% (52, 48%) |
| sl30_tp50 | -62% (991, 16%) | -20% (1277, 7%) | -44% (10, 10%) | -18% (52, 48%) |
| sl50_tp50 | -62% (991, 18%) | -21% (1277, 7%) | -47% (10, 10%) | -18% (52, 48%) |
| no_stop_tp100 | -61% (991, 16%) | -21% (1277, 7%) | -40% (10, 10%) | -16% (52, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 35433. Outcomes:

- missed_window: 22924
- low_liquidity: 6415
- proven_liquidity_gone: 2768
- no_momentum: 1332
- research_failed: 1007
- simulated failed buy: 437
- proven_low_volume: 393
- proven_price_collapsed_or_parabolic: 58
- proven: 53
- proven_no_uptrend: 24
- research_passed: 12
- dip: 10

Warning: 276 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
