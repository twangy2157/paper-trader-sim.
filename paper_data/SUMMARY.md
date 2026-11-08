# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T12:25:44Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1162 | 12% | -63.1% | -66 to -60 | -73463 |
| all momentum | 1178 | 13% | -62.7% | -66 to -59 | -74007 |
| control | 1535 | 6% | -19.1% | -21 to -17 | -29391 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1157, 13%) | -19% (1535, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1157, 14%) | -19% (1535, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -64% (1157, 15%) | -19% (1535, 7%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1157, 17%) | -20% (1535, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1157, 15%) | -20% (1535, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 41707. Outcomes:

- missed_window: 27279
- low_liquidity: 7219
- proven_liquidity_gone: 3229
- no_momentum: 1592
- research_failed: 1165
- proven_low_volume: 541
- simulated failed buy: 502
- proven_price_collapsed_or_parabolic: 73
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 313 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
