# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T16:25:44Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 73.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1183 | 12% | -63.4% | -67 to -60 | -75075 |
| all momentum | 1199 | 13% | -63.0% | -66 to -60 | -75619 |
| control | 1587 | 6% | -18.9% | -21 to -17 | -30186 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1178, 13%) | -19% (1587, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1178, 14%) | -19% (1587, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -65% (1178, 15%) | -19% (1587, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1178, 17%) | -19% (1587, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1178, 15%) | -20% (1587, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 42864. Outcomes:

- missed_window: 28078
- low_liquidity: 7375
- proven_liquidity_gone: 3324
- no_momentum: 1637
- research_failed: 1194
- proven_low_volume: 563
- simulated failed buy: 511
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 25
- research_passed: 16
- dip: 11

Warning: 321 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
