# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T03:09:09Z. Bankroll cash (research-selected trades): 899.0. Open positions: 37. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 67 | 15% | -39.6% | -55 to -25 | -2662 |
| all momentum | 68 | 15% | -40.5% | -56 to -26 | -2763 |
| control | 44 | 11% | -9.3% | -20 to 2 | -415 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -42% (47, 19%) | -9% (44, 11%) |
| wide_sl50_tp100 | -42% (47, 21%) | -11% (44, 11%) |
| sl30_tp50 | -47% (47, 21%) | -13% (44, 11%) |
| sl50_tp50 | -47% (47, 23%) | -12% (44, 14%) |
| no_stop_tp100 | -42% (47, 21%) | -11% (44, 11%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3634. Outcomes:

- missed_window: 2392
- low_liquidity: 1027
- no_momentum: 107
- research_failed: 85
- simulated failed buy: 22
- research_passed: 1

Warning: 13 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
