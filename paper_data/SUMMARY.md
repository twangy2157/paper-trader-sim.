# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T22:41:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 39. Pools on watchlist: 81.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1230 | 12% | -63.7% | -67 to -60 | -78427 |
| all momentum | 1246 | 13% | -63.3% | -67 to -60 | -78971 |
| control | 1660 | 5% | -18.8% | -21 to -17 | -31415 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 57 | 46% | -16.2% | -30 to -4 | -932 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1225, 13%) | -19% (1660, 5%) | -39% (12, 8%) | -16% (57, 46%) |
| wide_sl50_tp100 | -64% (1225, 14%) | -19% (1660, 6%) | -47% (12, 8%) | -16% (57, 46%) |
| sl30_tp50 | -65% (1225, 16%) | -19% (1660, 6%) | -42% (12, 8%) | -18% (57, 46%) |
| sl50_tp50 | -64% (1225, 17%) | -19% (1660, 7%) | -49% (12, 8%) | -18% (57, 46%) |
| no_stop_tp100 | -63% (1225, 15%) | -20% (1660, 6%) | -44% (12, 8%) | -16% (57, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 45074. Outcomes:

- missed_window: 29728
- low_liquidity: 7583
- proven_liquidity_gone: 3448
- no_momentum: 1733
- research_failed: 1237
- proven_low_volume: 611
- simulated failed buy: 544
- proven_price_collapsed_or_parabolic: 76
- proven: 60
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 354 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
