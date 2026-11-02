# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T15:49:08Z. Bankroll cash (research-selected trades): 898.5. Open positions: 12. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 147 | 14% | -51.4% | -61 to -42 | -7564 |
| all momentum | 148 | 14% | -51.7% | -61 to -41 | -7666 |
| control | 128 | 11% | -15.4% | -23 to -8 | -1979 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (127, 16%) | -15% (128, 11%) | - | - |
| wide_sl50_tp100 | -55% (127, 17%) | -16% (128, 11%) | - | - |
| sl30_tp50 | -55% (127, 20%) | -17% (128, 12%) | - | - |
| sl50_tp50 | -54% (127, 22%) | -17% (128, 12%) | - | - |
| no_stop_tp100 | -55% (127, 17%) | -17% (128, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5445. Outcomes:

- missed_window: 3592
- low_liquidity: 1439
- no_momentum: 178
- research_failed: 153
- simulated failed buy: 46
- proven_liquidity_gone: 33
- proven_low_volume: 3
- research_passed: 1

Warning: 29 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
