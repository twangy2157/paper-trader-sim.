# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T04:03:10Z. Bankroll cash (research-selected trades): 564.24568815387. Open positions: 22. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3231 | 11% | -67.0% | -69 to -65 | -216870 |
| all momentum | 3251 | 11% | -66.8% | -69 to -65 | -217305 |
| control | 3957 | 6% | -19.2% | -20 to -18 | -76255 |
| dip buy | 42 | 26% | -13.0% | -30 to 5 | -548 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3230, 11%) | -19% (3957, 6%) | -13% (42, 26%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3230, 13%) | -19% (3957, 7%) | -16% (42, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3230, 14%) | -19% (3957, 7%) | -17% (42, 31%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3230, 15%) | -20% (3957, 8%) | -18% (42, 36%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3230, 13%) | -20% (3957, 7%) | -15% (42, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 107249. Outcomes:

- missed_window: 69645
- low_liquidity: 17967
- proven_liquidity_gone: 9262
- no_momentum: 4010
- research_failed: 3241
- proven_low_volume: 1377
- simulated failed buy: 1339
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 42
- research_passed: 20

Warning: 845 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
