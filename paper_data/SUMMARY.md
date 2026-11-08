# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T18:59:12Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1204 | 12% | -63.6% | -67 to -60 | -76658 |
| all momentum | 1220 | 13% | -63.2% | -67 to -60 | -77202 |
| control | 1610 | 6% | -18.9% | -21 to -17 | -30549 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 57 | 46% | -16.2% | -30 to -4 | -932 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1199, 13%) | -19% (1610, 6%) | -39% (12, 8%) | -16% (57, 46%) |
| wide_sl50_tp100 | -63% (1199, 14%) | -19% (1610, 6%) | -47% (12, 8%) | -16% (57, 46%) |
| sl30_tp50 | -64% (1199, 16%) | -19% (1610, 6%) | -42% (12, 8%) | -18% (57, 46%) |
| sl50_tp50 | -64% (1199, 17%) | -19% (1610, 7%) | -49% (12, 8%) | -18% (57, 46%) |
| no_stop_tp100 | -63% (1199, 15%) | -20% (1610, 6%) | -44% (12, 8%) | -16% (57, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 43670. Outcomes:

- missed_window: 28672
- low_liquidity: 7459
- proven_liquidity_gone: 3370
- no_momentum: 1665
- research_failed: 1213
- proven_low_volume: 586
- simulated failed buy: 521
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 330 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
