# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T03:51:09Z. Bankroll cash (research-selected trades): 899.0. Open positions: 22. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 79 | 14% | -43.7% | -57 to -29 | -3458 |
| all momentum | 80 | 14% | -44.4% | -58 to -30 | -3559 |
| control | 58 | 14% | -9.0% | -20 to 1 | -529 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -47% (59, 17%) | -9% (58, 14%) |
| wide_sl50_tp100 | -47% (59, 19%) | -10% (58, 14%) |
| sl30_tp50 | -50% (59, 20%) | -13% (58, 14%) |
| sl50_tp50 | -50% (59, 22%) | -12% (58, 16%) |
| no_stop_tp100 | -48% (59, 19%) | -10% (58, 14%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3787. Outcomes:

- missed_window: 2499
- low_liquidity: 1058
- no_momentum: 110
- research_failed: 93
- simulated failed buy: 26
- research_passed: 1

Warning: 17 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
