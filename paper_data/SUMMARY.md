# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T04:43:11Z. Bankroll cash (research-selected trades): 899.0. Open positions: 25. Pools on watchlist: 35.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 90 | 13% | -46.8% | -59 to -33 | -4222 |
| all momentum | 91 | 13% | -47.4% | -59 to -34 | -4323 |
| control | 65 | 12% | -12.9% | -24 to -3 | -848 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -51% (70, 16%) | -13% (65, 12%) |
| wide_sl50_tp100 | -52% (70, 17%) | -14% (65, 12%) |
| sl30_tp50 | -53% (70, 20%) | -17% (65, 12%) |
| sl50_tp50 | -53% (70, 21%) | -16% (65, 14%) |
| no_stop_tp100 | -52% (70, 17%) | -14% (65, 12%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3991. Outcomes:

- missed_window: 2623
- low_liquidity: 1114
- no_momentum: 119
- research_failed: 105
- simulated failed buy: 29
- research_passed: 1

Warning: 20 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
