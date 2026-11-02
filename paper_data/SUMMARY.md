# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T02:37:00Z. Bankroll cash (research-selected trades): 899.0. Open positions: 37. Pools on watchlist: 52.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 58 | 14% | -38.2% | -54 to -22 | -2223 |
| all momentum | 59 | 14% | -39.3% | -56 to -23 | -2324 |
| control | 37 | 8% | -9.4% | -22 to 3 | -353 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -41% (38, 18%) | -9% (37, 8%) |
| wide_sl50_tp100 | -39% (38, 21%) | -11% (37, 8%) |
| sl30_tp50 | -47% (38, 21%) | -13% (37, 8%) |
| sl50_tp50 | -46% (38, 24%) | -11% (37, 11%) |
| no_stop_tp100 | -39% (38, 21%) | -12% (37, 8%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3485. Outcomes:

- missed_window: 2283
- low_liquidity: 1003
- no_momentum: 99
- research_failed: 77
- simulated failed buy: 22
- research_passed: 1

Warning: 13 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
