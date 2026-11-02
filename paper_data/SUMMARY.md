# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T15:28:39Z. Bankroll cash (research-selected trades): 898.5. Open positions: 13. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 144 | 15% | -50.5% | -61 to -40 | -7280 |
| all momentum | 145 | 14% | -50.8% | -60 to -41 | -7382 |
| control | 125 | 11% | -14.8% | -22 to -8 | -1857 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (124, 16%) | -15% (125, 11%) | - | - |
| wide_sl50_tp100 | -54% (124, 18%) | -16% (125, 11%) | - | - |
| sl30_tp50 | -54% (124, 20%) | -17% (125, 12%) | - | - |
| sl50_tp50 | -53% (124, 23%) | -17% (125, 13%) | - | - |
| no_stop_tp100 | -54% (124, 18%) | -16% (125, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5346. Outcomes:

- missed_window: 3528
- low_liquidity: 1424
- no_momentum: 175
- research_failed: 151
- simulated failed buy: 45
- proven_liquidity_gone: 20
- proven_low_volume: 2
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
