# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T15:18:33Z. Bankroll cash (research-selected trades): 898.5. Open positions: 17. Pools on watchlist: 80.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 141 | 14% | -50.8% | -60 to -41 | -7174 |
| all momentum | 142 | 14% | -51.2% | -61 to -41 | -7276 |
| control | 122 | 11% | -15.1% | -22 to -8 | -1852 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (121, 16%) | -15% (122, 11%) | - | - |
| wide_sl50_tp100 | -54% (121, 17%) | -16% (122, 11%) | - | - |
| sl30_tp50 | -54% (121, 20%) | -17% (122, 12%) | - | - |
| sl50_tp50 | -53% (121, 22%) | -17% (122, 13%) | - | - |
| no_stop_tp100 | -55% (121, 17%) | -16% (122, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5278. Outcomes:

- missed_window: 3473
- low_liquidity: 1419
- no_momentum: 174
- research_failed: 150
- simulated failed buy: 45
- proven_liquidity_gone: 14
- proven_low_volume: 2
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
