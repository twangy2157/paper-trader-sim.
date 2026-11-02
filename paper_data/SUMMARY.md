# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T04:21:40Z. Bankroll cash (research-selected trades): 899.0. Open positions: 18. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 87 | 14% | -45.0% | -58 to -32 | -3921 |
| all momentum | 88 | 14% | -45.6% | -58 to -32 | -4022 |
| control | 65 | 12% | -12.9% | -24 to -3 | -847 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -48% (67, 16%) | -13% (65, 12%) |
| wide_sl50_tp100 | -49% (67, 18%) | -14% (65, 12%) |
| sl30_tp50 | -50% (67, 21%) | -17% (65, 12%) |
| sl50_tp50 | -51% (67, 22%) | -16% (65, 14%) |
| no_stop_tp100 | -50% (67, 18%) | -14% (65, 12%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3904. Outcomes:

- missed_window: 2575
- low_liquidity: 1087
- no_momentum: 113
- research_failed: 101
- simulated failed buy: 27
- research_passed: 1

Warning: 19 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
