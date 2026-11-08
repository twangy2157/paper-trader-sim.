# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T14:51:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 70.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1173 | 12% | -63.3% | -67 to -60 | -74327 |
| all momentum | 1189 | 13% | -62.9% | -66 to -59 | -74870 |
| control | 1564 | 6% | -19.0% | -21 to -17 | -29870 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1168, 13%) | -19% (1564, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1168, 14%) | -19% (1564, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -65% (1168, 15%) | -19% (1564, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1168, 17%) | -20% (1564, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1168, 15%) | -20% (1564, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 42356. Outcomes:

- missed_window: 27711
- low_liquidity: 7318
- proven_liquidity_gone: 3280
- no_momentum: 1624
- research_failed: 1180
- proven_low_volume: 555
- simulated failed buy: 508
- proven_price_collapsed_or_parabolic: 73
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 318 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
