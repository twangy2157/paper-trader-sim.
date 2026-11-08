# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T17:07:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1190 | 12% | -63.5% | -67 to -60 | -75650 |
| all momentum | 1206 | 13% | -63.1% | -66 to -60 | -76194 |
| control | 1591 | 6% | -18.9% | -21 to -17 | -30211 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1185, 13%) | -19% (1591, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1185, 14%) | -19% (1591, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -65% (1185, 15%) | -19% (1591, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1185, 17%) | -19% (1591, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1185, 15%) | -20% (1591, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 43068. Outcomes:

- missed_window: 28216
- low_liquidity: 7405
- proven_liquidity_gone: 3335
- no_momentum: 1646
- research_failed: 1201
- proven_low_volume: 567
- simulated failed buy: 515
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 25
- research_passed: 16
- dip: 12

Warning: 325 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
