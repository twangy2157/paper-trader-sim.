# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T18:12:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 88.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1201 | 12% | -63.6% | -67 to -60 | -76495 |
| all momentum | 1217 | 13% | -63.2% | -66 to -60 | -77039 |
| control | 1602 | 6% | -18.9% | -21 to -17 | -30370 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1196, 13%) | -19% (1602, 6%) | -39% (12, 8%) | -16% (56, 46%) |
| wide_sl50_tp100 | -64% (1196, 14%) | -19% (1602, 6%) | -47% (12, 8%) | -16% (56, 46%) |
| sl30_tp50 | -65% (1196, 16%) | -19% (1602, 6%) | -42% (12, 8%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1196, 17%) | -19% (1602, 7%) | -49% (12, 8%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1196, 15%) | -20% (1602, 6%) | -44% (12, 8%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 43461. Outcomes:

- missed_window: 28508
- low_liquidity: 7447
- proven_liquidity_gone: 3360
- no_momentum: 1658
- research_failed: 1207
- proven_low_volume: 578
- simulated failed buy: 519
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 328 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
