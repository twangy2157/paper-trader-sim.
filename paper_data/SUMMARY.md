# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T03:39:41Z. Bankroll cash (research-selected trades): 899.0. Open positions: 26. Pools on watchlist: 35.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 76 | 14% | -42.6% | -57 to -29 | -3243 |
| all momentum | 77 | 14% | -43.3% | -57 to -29 | -3344 |
| control | 53 | 9% | -12.5% | -23 to -2 | -668 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -46% (56, 18%) | -12% (53, 9%) |
| wide_sl50_tp100 | -46% (56, 20%) | -14% (53, 9%) |
| sl30_tp50 | -50% (56, 20%) | -16% (53, 9%) |
| sl50_tp50 | -51% (56, 21%) | -15% (53, 11%) |
| no_stop_tp100 | -46% (56, 20%) | -14% (53, 9%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3751. Outcomes:

- missed_window: 2472
- low_liquidity: 1054
- no_momentum: 109
- research_failed: 90
- simulated failed buy: 25
- research_passed: 1

Warning: 16 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
