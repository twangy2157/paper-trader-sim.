# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T18:22:44Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 81.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1202 | 12% | -63.6% | -67 to -60 | -76528 |
| all momentum | 1218 | 13% | -63.2% | -66 to -60 | -77072 |
| control | 1604 | 6% | -18.9% | -21 to -17 | -30414 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1197, 13%) | -19% (1604, 6%) | -39% (12, 8%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1197, 14%) | -19% (1604, 6%) | -47% (12, 8%) | -16% (56, 46%) |
| sl30_tp50 | -64% (1197, 16%) | -19% (1604, 6%) | -42% (12, 8%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1197, 17%) | -19% (1604, 7%) | -49% (12, 8%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1197, 15%) | -20% (1604, 6%) | -44% (12, 8%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 43527. Outcomes:

- missed_window: 28558
- low_liquidity: 7452
- proven_liquidity_gone: 3363
- no_momentum: 1661
- research_failed: 1209
- proven_low_volume: 580
- simulated failed buy: 520
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 329 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
