# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T04:54:30Z. Bankroll cash (research-selected trades): 899.0. Open positions: 23. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 94 | 15% | -46.3% | -58 to -33 | -4358 |
| all momentum | 95 | 15% | -46.9% | -59 to -34 | -4459 |
| control | 66 | 12% | -12.9% | -23 to -3 | -858 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -50% (74, 18%) | -13% (66, 12%) |
| wide_sl50_tp100 | -51% (74, 19%) | -14% (66, 12%) |
| sl30_tp50 | -52% (74, 22%) | -17% (66, 12%) |
| sl50_tp50 | -53% (74, 23%) | -16% (66, 14%) |
| no_stop_tp100 | -51% (74, 19%) | -14% (66, 12%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4018. Outcomes:

- missed_window: 2636
- low_liquidity: 1123
- no_momentum: 120
- research_failed: 107
- simulated failed buy: 31
- research_passed: 1

Warning: 22 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
