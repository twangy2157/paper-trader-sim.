# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T02:26:56Z. Bankroll cash (research-selected trades): 899.0. Open positions: 29. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 57 | 14% | -37.1% | -53 to -20 | -2123 |
| all momentum | 58 | 14% | -38.2% | -55 to -21 | -2224 |
| control | 37 | 8% | -9.4% | -22 to 3 | -353 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -39% (37, 19%) | -9% (37, 8%) |
| wide_sl50_tp100 | -38% (37, 22%) | -11% (37, 8%) |
| sl30_tp50 | -45% (37, 22%) | -13% (37, 8%) |
| sl50_tp50 | -45% (37, 24%) | -11% (37, 11%) |
| no_stop_tp100 | -37% (37, 22%) | -12% (37, 8%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3438. Outcomes:

- missed_window: 2252
- low_liquidity: 996
- no_momentum: 96
- research_failed: 71
- simulated failed buy: 22
- research_passed: 1

Warning: 13 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
