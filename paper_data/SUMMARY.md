# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T22:21:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 29. Pools on watchlist: 107.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1229 | 12% | -63.6% | -67 to -61 | -78326 |
| all momentum | 1245 | 13% | -63.3% | -67 to -60 | -78870 |
| control | 1655 | 5% | -18.9% | -21 to -17 | -31374 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 57 | 46% | -16.2% | -30 to -4 | -932 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1224, 13%) | -19% (1655, 5%) | -39% (12, 8%) | -16% (57, 46%) |
| wide_sl50_tp100 | -64% (1224, 14%) | -19% (1655, 6%) | -47% (12, 8%) | -16% (57, 46%) |
| sl30_tp50 | -65% (1224, 16%) | -19% (1655, 6%) | -42% (12, 8%) | -18% (57, 46%) |
| sl50_tp50 | -64% (1224, 17%) | -19% (1655, 7%) | -49% (12, 8%) | -18% (57, 46%) |
| no_stop_tp100 | -63% (1224, 15%) | -20% (1655, 6%) | -44% (12, 8%) | -16% (57, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 44919. Outcomes:

- missed_window: 29607
- low_liquidity: 7571
- proven_liquidity_gone: 3446
- no_momentum: 1721
- research_failed: 1233
- proven_low_volume: 608
- simulated failed buy: 543
- proven_price_collapsed_or_parabolic: 76
- proven: 60
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 353 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
