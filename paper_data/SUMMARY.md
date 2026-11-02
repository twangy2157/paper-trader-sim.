# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T13:18:44Z. Bankroll cash (research-selected trades): 898.5. Open positions: 8. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 127 | 14% | -50.4% | -61 to -40 | -6410 |
| all momentum | 128 | 14% | -50.8% | -61 to -41 | -6512 |
| control | 104 | 12% | -16.0% | -24 to -8 | -1678 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (107, 16%) | -16% (104, 12%) | - | - |
| wide_sl50_tp100 | -55% (107, 17%) | -17% (104, 12%) | - | - |
| sl30_tp50 | -54% (107, 20%) | -18% (104, 12%) | - | - |
| sl50_tp50 | -54% (107, 21%) | -18% (104, 13%) | - | - |
| no_stop_tp100 | -56% (107, 17%) | -17% (104, 12%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4656. Outcomes:

- missed_window: 3054
- low_liquidity: 1276
- no_momentum: 154
- research_failed: 129
- simulated failed buy: 42
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
