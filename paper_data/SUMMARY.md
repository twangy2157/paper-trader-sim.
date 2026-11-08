# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T16:57:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 28. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1187 | 12% | -63.4% | -67 to -60 | -75349 |
| all momentum | 1203 | 13% | -63.0% | -66 to -60 | -75892 |
| control | 1589 | 6% | -18.9% | -21 to -17 | -30196 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1182, 13%) | -19% (1589, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1182, 14%) | -19% (1589, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -65% (1182, 15%) | -19% (1589, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1182, 17%) | -19% (1589, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1182, 15%) | -20% (1589, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 43008. Outcomes:

- missed_window: 28167
- low_liquidity: 7402
- proven_liquidity_gone: 3330
- no_momentum: 1646
- research_failed: 1200
- proven_low_volume: 566
- simulated failed buy: 514
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 25
- research_passed: 16
- dip: 12

Warning: 324 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
