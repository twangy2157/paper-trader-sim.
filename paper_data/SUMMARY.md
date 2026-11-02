# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T04:11:35Z. Bankroll cash (research-selected trades): 899.0. Open positions: 17. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 85 | 13% | -46.7% | -60 to -34 | -3975 |
| all momentum | 86 | 13% | -47.3% | -60 to -35 | -4076 |
| control | 63 | 13% | -11.6% | -22 to -2 | -739 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -51% (65, 15%) | -12% (63, 13%) |
| wide_sl50_tp100 | -51% (65, 17%) | -13% (63, 13%) |
| sl30_tp50 | -53% (65, 18%) | -16% (63, 13%) |
| sl50_tp50 | -54% (65, 20%) | -15% (63, 14%) |
| no_stop_tp100 | -51% (65, 17%) | -13% (63, 13%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3863. Outcomes:

- missed_window: 2549
- low_liquidity: 1078
- no_momentum: 111
- research_failed: 98
- simulated failed buy: 26
- research_passed: 1

Warning: 18 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
