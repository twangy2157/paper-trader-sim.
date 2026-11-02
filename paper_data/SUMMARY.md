# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T14:02:45Z. Bankroll cash (research-selected trades): 898.5. Open positions: 22. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 128 | 14% | -50.8% | -60 to -41 | -6511 |
| all momentum | 129 | 14% | -51.2% | -61 to -41 | -6613 |
| control | 109 | 12% | -14.7% | -23 to -7 | -1616 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (108, 16%) | -15% (109, 12%) | - | - |
| wide_sl50_tp100 | -55% (108, 17%) | -15% (109, 12%) | - | - |
| sl30_tp50 | -55% (108, 19%) | -17% (109, 13%) | - | - |
| sl50_tp50 | -55% (108, 21%) | -17% (109, 14%) | - | - |
| no_stop_tp100 | -56% (108, 17%) | -16% (109, 12%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4851. Outcomes:

- missed_window: 3165
- low_liquidity: 1338
- no_momentum: 164
- research_failed: 139
- simulated failed buy: 44
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
