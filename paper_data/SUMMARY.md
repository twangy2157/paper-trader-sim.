# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T14:13:43Z. Bankroll cash (research-selected trades): 898.5. Open positions: 24. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 129 | 14% | -51.1% | -61 to -40 | -6602 |
| all momentum | 130 | 14% | -51.5% | -61 to -41 | -6704 |
| control | 110 | 12% | -15.0% | -23 to -7 | -1662 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (109, 16%) | -15% (110, 12%) | - | - |
| wide_sl50_tp100 | -56% (109, 17%) | -16% (110, 12%) | - | - |
| sl30_tp50 | -55% (109, 19%) | -17% (110, 13%) | - | - |
| sl50_tp50 | -55% (109, 21%) | -17% (110, 14%) | - | - |
| no_stop_tp100 | -56% (109, 17%) | -16% (110, 12%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4898. Outcomes:

- missed_window: 3194
- low_liquidity: 1352
- no_momentum: 166
- research_failed: 141
- simulated failed buy: 44
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
