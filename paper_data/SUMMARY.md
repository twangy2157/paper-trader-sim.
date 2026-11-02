# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T02:15:45Z. Bankroll cash (research-selected trades): 899.0. Open positions: 24. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 56 | 14% | -37.2% | -55 to -21 | -2087 |
| all momentum | 57 | 14% | -38.3% | -55 to -22 | -2188 |
| control | 36 | 8% | -9.4% | -22 to 3 | -344 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -39% (36, 19%) | -9% (36, 8%) |
| wide_sl50_tp100 | -37% (36, 22%) | -11% (36, 8%) |
| sl30_tp50 | -46% (36, 22%) | -13% (36, 8%) |
| sl50_tp50 | -45% (36, 25%) | -12% (36, 11%) |
| no_stop_tp100 | -37% (36, 22%) | -12% (36, 8%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3406. Outcomes:

- missed_window: 2239
- low_liquidity: 985
- no_momentum: 91
- research_failed: 69
- simulated failed buy: 21
- research_passed: 1

Warning: 13 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
