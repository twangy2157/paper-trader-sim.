# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T17:52:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 82.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1199 | 12% | -63.7% | -67 to -60 | -76456 |
| all momentum | 1215 | 13% | -63.3% | -66 to -60 | -77000 |
| control | 1601 | 6% | -18.9% | -21 to -17 | -30367 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1194, 13%) | -19% (1601, 6%) | -39% (12, 8%) | -16% (56, 46%) |
| wide_sl50_tp100 | -64% (1194, 14%) | -19% (1601, 6%) | -47% (12, 8%) | -16% (56, 46%) |
| sl30_tp50 | -65% (1194, 15%) | -19% (1601, 6%) | -42% (12, 8%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1194, 17%) | -19% (1601, 7%) | -49% (12, 8%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1194, 15%) | -20% (1601, 6%) | -44% (12, 8%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 43336. Outcomes:

- missed_window: 28423
- low_liquidity: 7427
- proven_liquidity_gone: 3356
- no_momentum: 1654
- research_failed: 1204
- proven_low_volume: 570
- simulated failed buy: 518
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 328 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
