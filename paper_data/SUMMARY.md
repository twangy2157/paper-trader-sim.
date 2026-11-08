# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T21:39:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1223 | 12% | -63.5% | -67 to -60 | -77805 |
| all momentum | 1239 | 13% | -63.1% | -66 to -60 | -78349 |
| control | 1645 | 6% | -18.9% | -21 to -17 | -31299 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 57 | 46% | -16.2% | -30 to -4 | -932 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1218, 13%) | -19% (1645, 6%) | -39% (12, 8%) | -16% (57, 46%) |
| wide_sl50_tp100 | -63% (1218, 14%) | -19% (1645, 6%) | -47% (12, 8%) | -16% (57, 46%) |
| sl30_tp50 | -64% (1218, 16%) | -19% (1645, 6%) | -42% (12, 8%) | -18% (57, 46%) |
| sl50_tp50 | -64% (1218, 17%) | -19% (1645, 7%) | -49% (12, 8%) | -18% (57, 46%) |
| no_stop_tp100 | -63% (1218, 15%) | -20% (1645, 6%) | -44% (12, 8%) | -16% (57, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 44679. Outcomes:

- missed_window: 29432
- low_liquidity: 7554
- proven_liquidity_gone: 3428
- no_momentum: 1704
- research_failed: 1230
- proven_low_volume: 602
- simulated failed buy: 540
- proven_price_collapsed_or_parabolic: 76
- proven: 59
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 350 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
