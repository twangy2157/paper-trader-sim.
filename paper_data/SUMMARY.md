# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T17:19:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 86.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1194 | 12% | -63.5% | -67 to -60 | -75954 |
| all momentum | 1210 | 13% | -63.1% | -66 to -60 | -76498 |
| control | 1593 | 6% | -18.9% | -21 to -17 | -30305 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1189, 13%) | -19% (1593, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1189, 14%) | -19% (1593, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -65% (1189, 15%) | -19% (1593, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1189, 17%) | -19% (1593, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1189, 15%) | -20% (1593, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 43123. Outcomes:

- missed_window: 28258
- low_liquidity: 7409
- proven_liquidity_gone: 3340
- no_momentum: 1648
- research_failed: 1202
- proven_low_volume: 568
- simulated failed buy: 515
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 25
- research_passed: 16
- dip: 12

Warning: 325 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
