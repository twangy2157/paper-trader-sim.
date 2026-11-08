# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T12:53:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 12. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1164 | 12% | -63.2% | -67 to -60 | -73664 |
| all momentum | 1180 | 13% | -62.8% | -66 to -59 | -74208 |
| control | 1540 | 6% | -19.0% | -21 to -17 | -29430 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1159, 13%) | -19% (1540, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1159, 14%) | -19% (1540, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -64% (1159, 15%) | -19% (1540, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1159, 17%) | -20% (1540, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1159, 15%) | -20% (1540, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 41795. Outcomes:

- missed_window: 27343
- low_liquidity: 7230
- proven_liquidity_gone: 3237
- no_momentum: 1593
- research_failed: 1167
- proven_low_volume: 543
- simulated failed buy: 502
- proven_price_collapsed_or_parabolic: 73
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 313 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
