# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T10:39:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1143 | 13% | -62.9% | -66 to -60 | -71966 |
| all momentum | 1159 | 13% | -62.5% | -66 to -59 | -72510 |
| control | 1515 | 6% | -19.1% | -21 to -17 | -29102 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1138, 13%) | -19% (1515, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1138, 14%) | -19% (1515, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -64% (1138, 16%) | -19% (1515, 7%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1138, 17%) | -20% (1515, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1138, 15%) | -20% (1515, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 41226. Outcomes:

- missed_window: 26952
- low_liquidity: 7155
- proven_liquidity_gone: 3191
- no_momentum: 1572
- research_failed: 1150
- proven_low_volume: 530
- simulated failed buy: 498
- proven_price_collapsed_or_parabolic: 71
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 313 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
