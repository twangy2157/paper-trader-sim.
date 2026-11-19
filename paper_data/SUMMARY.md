# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-19T20:05:13Z. Bankroll cash (research-selected trades): 348.8536238229275. Open positions: 18. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3198 | 11% | -67.2% | -69 to -65 | -215091 |
| all momentum | 3215 | 11% | -67.0% | -69 to -65 | -215542 |
| control | 3917 | 6% | -19.2% | -20 to -18 | -75370 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3194, 11%) | -19% (3917, 6%) | -12% (41, 27%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3194, 13%) | -19% (3917, 7%) | -15% (41, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3194, 14%) | -19% (3917, 7%) | -18% (41, 29%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3194, 15%) | -20% (3917, 8%) | -19% (41, 34%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3194, 13%) | -20% (3917, 7%) | -13% (41, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 106053. Outcomes:

- missed_window: 68932
- low_liquidity: 17723
- proven_liquidity_gone: 9124
- no_momentum: 3969
- research_failed: 3206
- proven_low_volume: 1369
- simulated failed buy: 1329
- proven_price_collapsed_or_parabolic: 157
- proven: 123
- proven_no_uptrend: 61
- dip: 41
- research_passed: 19

Warning: 839 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
