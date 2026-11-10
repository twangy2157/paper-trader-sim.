# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T16:40:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 31. Pools on watchlist: 37.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1561 | 12% | -64.0% | -67 to -61 | -100000 |
| all momentum | 1577 | 12% | -63.7% | -66 to -61 | -100544 |
| control | 2257 | 5% | -18.1% | -20 to -17 | -41130 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1556, 12%) | -18% (2257, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1556, 14%) | -18% (2257, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1556, 15%) | -18% (2257, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1556, 17%) | -19% (2257, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1556, 15%) | -19% (2257, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 57345. Outcomes:

- missed_window: 38106
- low_liquidity: 9162
- proven_liquidity_gone: 4312
- no_momentum: 2319
- research_failed: 1574
- proven_low_volume: 901
- simulated failed buy: 726
- proven_price_collapsed_or_parabolic: 100
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 489 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
