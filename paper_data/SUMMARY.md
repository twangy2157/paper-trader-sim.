# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T17:40:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 84.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1197 | 12% | -63.6% | -67 to -60 | -76255 |
| all momentum | 1213 | 13% | -63.2% | -67 to -60 | -76798 |
| control | 1596 | 6% | -18.9% | -21 to -17 | -30327 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1192, 13%) | -19% (1596, 6%) | -39% (12, 8%) | -16% (56, 46%) |
| wide_sl50_tp100 | -64% (1192, 14%) | -19% (1596, 6%) | -47% (12, 8%) | -16% (56, 46%) |
| sl30_tp50 | -65% (1192, 15%) | -19% (1596, 6%) | -42% (12, 8%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1192, 17%) | -19% (1596, 7%) | -49% (12, 8%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1192, 15%) | -20% (1596, 6%) | -44% (12, 8%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 43259. Outcomes:

- missed_window: 28360
- low_liquidity: 7422
- proven_liquidity_gone: 3349
- no_momentum: 1653
- research_failed: 1204
- proven_low_volume: 570
- simulated failed buy: 517
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 327 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
