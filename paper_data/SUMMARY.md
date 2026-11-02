# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T15:38:53Z. Bankroll cash (research-selected trades): 898.5. Open positions: 13. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 146 | 14% | -51.2% | -61 to -41 | -7481 |
| all momentum | 147 | 14% | -51.5% | -61 to -41 | -7582 |
| control | 125 | 11% | -14.8% | -22 to -8 | -1857 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (126, 16%) | -15% (125, 11%) | - | - |
| wide_sl50_tp100 | -55% (126, 17%) | -16% (125, 11%) | - | - |
| sl30_tp50 | -55% (126, 20%) | -17% (125, 12%) | - | - |
| sl50_tp50 | -54% (126, 22%) | -17% (125, 13%) | - | - |
| no_stop_tp100 | -55% (126, 17%) | -16% (125, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5396. Outcomes:

- missed_window: 3560
- low_liquidity: 1433
- no_momentum: 175
- research_failed: 153
- simulated failed buy: 45
- proven_liquidity_gone: 26
- proven_low_volume: 3
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
