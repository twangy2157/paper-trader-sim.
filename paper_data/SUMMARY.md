# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T05:46:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1102 | 13% | -61.7% | -65 to -58 | -68116 |
| all momentum | 1118 | 13% | -61.3% | -65 to -58 | -68659 |
| control | 1481 | 6% | -19.1% | -21 to -17 | -28487 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 55 | 47% | -14.9% | -27 to -2 | -826 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1097, 13%) | -19% (1481, 6%) | -41% (11, 9%) | -15% (55, 47%) |
| wide_sl50_tp100 | -62% (1097, 15%) | -20% (1481, 6%) | -48% (11, 9%) | -15% (55, 47%) |
| sl30_tp50 | -63% (1097, 16%) | -19% (1481, 7%) | -44% (11, 9%) | -17% (55, 47%) |
| sl50_tp50 | -63% (1097, 18%) | -20% (1481, 7%) | -52% (11, 9%) | -17% (55, 47%) |
| no_stop_tp100 | -62% (1097, 16%) | -20% (1481, 6%) | -45% (11, 9%) | -15% (55, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 39996. Outcomes:

- missed_window: 26165
- low_liquidity: 6953
- proven_liquidity_gone: 3063
- no_momentum: 1538
- research_failed: 1109
- proven_low_volume: 511
- simulated failed buy: 479
- proven_price_collapsed_or_parabolic: 71
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 302 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
