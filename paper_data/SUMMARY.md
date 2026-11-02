# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T05:04:35Z. Bankroll cash (research-selected trades): 899.0. Open positions: 25. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 96 | 16% | -46.3% | -58 to -34 | -4456 |
| all momentum | 97 | 15% | -46.9% | -59 to -35 | -4557 |
| control | 67 | 12% | -12.7% | -23 to -2 | -861 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -50% (76, 18%) | -13% (67, 12%) |
| wide_sl50_tp100 | -51% (76, 20%) | -14% (67, 12%) |
| sl30_tp50 | -52% (76, 22%) | -16% (67, 12%) |
| sl50_tp50 | -53% (76, 24%) | -16% (67, 13%) |
| no_stop_tp100 | -51% (76, 20%) | -14% (67, 12%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4051. Outcomes:

- missed_window: 2653
- low_liquidity: 1134
- no_momentum: 124
- research_failed: 108
- simulated failed buy: 31
- research_passed: 1

Warning: 22 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
