# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T23:03:14Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 35. Pools on watchlist: 107.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1231 | 12% | -63.6% | -67 to -60 | -78435 |
| all momentum | 1247 | 13% | -63.2% | -66 to -60 | -78979 |
| control | 1668 | 5% | -18.8% | -20 to -17 | -31479 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 58 | 45% | -17.7% | -31 to -5 | -1032 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1226, 13%) | -19% (1668, 5%) | -39% (12, 8%) | -18% (58, 45%) |
| wide_sl50_tp100 | -63% (1226, 14%) | -19% (1668, 6%) | -47% (12, 8%) | -18% (58, 45%) |
| sl30_tp50 | -65% (1226, 15%) | -19% (1668, 6%) | -42% (12, 8%) | -19% (58, 45%) |
| sl50_tp50 | -64% (1226, 17%) | -19% (1668, 7%) | -49% (12, 8%) | -19% (58, 45%) |
| no_stop_tp100 | -63% (1226, 15%) | -19% (1668, 6%) | -44% (12, 8%) | -18% (58, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 45225. Outcomes:

- missed_window: 29849
- low_liquidity: 7597
- proven_liquidity_gone: 3455
- no_momentum: 1738
- research_failed: 1238
- proven_low_volume: 614
- simulated failed buy: 544
- proven_price_collapsed_or_parabolic: 76
- proven: 60
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 355 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
