# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T02:05:40Z. Bankroll cash (research-selected trades): 899.0. Open positions: 21. Pools on watchlist: 23.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 55 | 15% | -36.0% | -53 to -19 | -1987 |
| all momentum | 56 | 14% | -37.2% | -54 to -20 | -2088 |
| control | 34 | 9% | -9.6% | -23 to 4 | -332 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -37% (35, 20%) | -10% (34, 9%) |
| wide_sl50_tp100 | -36% (35, 23%) | -12% (34, 9%) |
| sl30_tp50 | -44% (35, 23%) | -13% (34, 9%) |
| sl50_tp50 | -43% (35, 26%) | -12% (34, 12%) |
| no_stop_tp100 | -35% (35, 23%) | -12% (34, 9%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3383. Outcomes:

- missed_window: 2233
- low_liquidity: 976
- no_momentum: 87
- research_failed: 67
- simulated failed buy: 19
- research_passed: 1

Warning: 12 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
