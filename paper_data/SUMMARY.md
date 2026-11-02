# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T02:47:35Z. Bankroll cash (research-selected trades): 899.0. Open positions: 38. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 61 | 13% | -38.7% | -54 to -22 | -2368 |
| all momentum | 62 | 13% | -39.7% | -56 to -24 | -2469 |
| control | 39 | 8% | -9.3% | -21 to 2 | -369 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -41% (41, 17%) | -9% (39, 8%) |
| wide_sl50_tp100 | -41% (41, 20%) | -11% (39, 8%) |
| sl30_tp50 | -47% (41, 20%) | -13% (39, 8%) |
| sl50_tp50 | -47% (41, 22%) | -11% (39, 10%) |
| no_stop_tp100 | -41% (41, 20%) | -12% (39, 8%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3525. Outcomes:

- missed_window: 2309
- low_liquidity: 1011
- no_momentum: 102
- research_failed: 80
- simulated failed buy: 22
- research_passed: 1

Warning: 13 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
