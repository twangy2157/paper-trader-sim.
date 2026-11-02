# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T04:32:00Z. Bankroll cash (research-selected trades): 899.0. Open positions: 21. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 89 | 13% | -46.2% | -59 to -32 | -4121 |
| all momentum | 90 | 13% | -46.8% | -59 to -33 | -4222 |
| control | 65 | 12% | -12.9% | -24 to -3 | -847 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -50% (69, 16%) | -13% (65, 12%) |
| wide_sl50_tp100 | -51% (69, 17%) | -14% (65, 12%) |
| sl30_tp50 | -52% (69, 20%) | -17% (65, 12%) |
| sl50_tp50 | -53% (69, 22%) | -16% (65, 14%) |
| no_stop_tp100 | -51% (69, 17%) | -14% (65, 12%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3941. Outcomes:

- missed_window: 2592
- low_liquidity: 1101
- no_momentum: 116
- research_failed: 103
- simulated failed buy: 28
- research_passed: 1

Warning: 19 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
