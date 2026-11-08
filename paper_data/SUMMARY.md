# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T07:33:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1112 | 13% | -62.0% | -65 to -58 | -69023 |
| all momentum | 1128 | 13% | -61.6% | -65 to -58 | -69567 |
| control | 1496 | 6% | -19.1% | -21 to -17 | -28770 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 55 | 47% | -14.9% | -27 to -2 | -826 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1107, 13%) | -19% (1496, 6%) | -41% (11, 9%) | -15% (55, 47%) |
| wide_sl50_tp100 | -62% (1107, 15%) | -20% (1496, 6%) | -48% (11, 9%) | -15% (55, 47%) |
| sl30_tp50 | -63% (1107, 16%) | -19% (1496, 6%) | -44% (11, 9%) | -17% (55, 47%) |
| sl50_tp50 | -63% (1107, 18%) | -20% (1496, 7%) | -52% (11, 9%) | -17% (55, 47%) |
| no_stop_tp100 | -62% (1107, 16%) | -20% (1496, 6%) | -45% (11, 9%) | -15% (55, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 40421. Outcomes:

- missed_window: 26447
- low_liquidity: 7018
- proven_liquidity_gone: 3108
- no_momentum: 1542
- research_failed: 1126
- proven_low_volume: 517
- simulated failed buy: 485
- proven_price_collapsed_or_parabolic: 71
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 303 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
