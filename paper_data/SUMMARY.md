# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T06:29:21Z. Bankroll cash (research-selected trades): 898.5. Open positions: 23. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 113 | 14% | -48.3% | -60 to -37 | -5464 |
| all momentum | 114 | 14% | -48.7% | -60 to -37 | -5565 |
| control | 84 | 11% | -17.0% | -26 to -8 | -1435 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -51% (93, 16%) | -17% (84, 11%) |
| wide_sl50_tp100 | -53% (93, 17%) | -18% (84, 11%) |
| sl30_tp50 | -53% (93, 19%) | -20% (84, 11%) |
| sl50_tp50 | -53% (93, 22%) | -19% (84, 12%) |
| no_stop_tp100 | -54% (93, 17%) | -18% (84, 11%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4381. Outcomes:

- missed_window: 2861
- low_liquidity: 1216
- no_momentum: 140
- research_failed: 124
- simulated failed buy: 39
- research_passed: 1

Warning: 27 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
