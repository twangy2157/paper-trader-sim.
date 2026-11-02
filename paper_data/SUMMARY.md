# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T01:45:30Z. Bankroll cash (research-selected trades): 899.0. Open positions: 16. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 53 | 15% | -33.6% | -50 to -16 | -1786 |
| all momentum | 54 | 15% | -34.8% | -52 to -17 | -1887 |
| control | 31 | 10% | -9.9% | -25 to 5 | -311 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -34% (33, 21%) | -10% (31, 10%) |
| wide_sl50_tp100 | -32% (33, 24%) | -12% (31, 10%) |
| sl30_tp50 | -41% (33, 24%) | -14% (31, 10%) |
| sl50_tp50 | -40% (33, 27%) | -12% (31, 13%) |
| no_stop_tp100 | -31% (33, 24%) | -13% (31, 10%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3274. Outcomes:

- missed_window: 2157
- low_liquidity: 953
- no_momentum: 83
- research_failed: 61
- simulated failed buy: 19
- research_passed: 1

Warning: 11 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
