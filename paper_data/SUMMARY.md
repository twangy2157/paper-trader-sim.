# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T06:40:40Z. Bankroll cash (research-selected trades): 898.5. Open positions: 27. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 115 | 14% | -48.4% | -59 to -37 | -5571 |
| all momentum | 116 | 14% | -48.8% | -60 to -37 | -5672 |
| control | 84 | 11% | -17.0% | -26 to -8 | -1435 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -51% (95, 16%) | -17% (84, 11%) |
| wide_sl50_tp100 | -53% (95, 17%) | -18% (84, 11%) |
| sl30_tp50 | -53% (95, 19%) | -20% (84, 11%) |
| sl50_tp50 | -53% (95, 21%) | -19% (84, 12%) |
| no_stop_tp100 | -54% (95, 17%) | -18% (84, 11%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4425. Outcomes:

- missed_window: 2884
- low_liquidity: 1230
- no_momentum: 144
- research_failed: 126
- simulated failed buy: 40
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
