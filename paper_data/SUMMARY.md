# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T03:29:36Z. Bankroll cash (research-selected trades): 899.0. Open positions: 32. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 71 | 14% | -40.8% | -55 to -26 | -2907 |
| all momentum | 72 | 14% | -41.7% | -56 to -27 | -3008 |
| control | 51 | 10% | -10.9% | -21 to -0 | -561 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -44% (51, 18%) | -11% (51, 10%) |
| wide_sl50_tp100 | -44% (51, 20%) | -12% (51, 10%) |
| sl30_tp50 | -48% (51, 20%) | -14% (51, 10%) |
| sl50_tp50 | -49% (51, 22%) | -13% (51, 12%) |
| no_stop_tp100 | -44% (51, 20%) | -13% (51, 10%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3701. Outcomes:

- missed_window: 2433
- low_liquidity: 1044
- no_momentum: 109
- research_failed: 89
- simulated failed buy: 25
- research_passed: 1

Warning: 16 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
