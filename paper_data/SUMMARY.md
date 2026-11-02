# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T16:10:39Z. Bankroll cash (research-selected trades): 898.5. Open positions: 21. Pools on watchlist: 33.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 147 | 14% | -51.4% | -61 to -42 | -7564 |
| all momentum | 148 | 14% | -51.7% | -61 to -41 | -7666 |
| control | 129 | 11% | -15.4% | -22 to -8 | -1992 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (127, 16%) | -15% (129, 11%) | - | - |
| wide_sl50_tp100 | -55% (127, 17%) | -16% (129, 11%) | - | - |
| sl30_tp50 | -55% (127, 20%) | -17% (129, 12%) | - | - |
| sl50_tp50 | -54% (127, 22%) | -17% (129, 12%) | - | - |
| no_stop_tp100 | -55% (127, 17%) | -17% (129, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5563. Outcomes:

- missed_window: 3667
- low_liquidity: 1455
- no_momentum: 182
- research_failed: 159
- simulated failed buy: 48
- proven_liquidity_gone: 46
- proven_low_volume: 5
- research_passed: 1

Warning: 31 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
