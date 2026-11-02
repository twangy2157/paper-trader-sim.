# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T17:13:10Z. Bankroll cash (research-selected trades): 898.5. Open positions: 21. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 159 | 15% | -51.6% | -61 to -42 | -8224 |
| all momentum | 160 | 15% | -51.9% | -61 to -42 | -8326 |
| control | 138 | 11% | -15.4% | -22 to -9 | -2141 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (139, 17%) | -15% (138, 11%) | - | - |
| wide_sl50_tp100 | -55% (139, 18%) | -16% (138, 11%) | - | - |
| sl30_tp50 | -55% (139, 20%) | -18% (138, 12%) | - | - |
| sl50_tp50 | -55% (139, 22%) | -17% (138, 12%) | - | - |
| no_stop_tp100 | -54% (139, 19%) | -17% (138, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5838. Outcomes:

- missed_window: 3842
- low_liquidity: 1513
- no_momentum: 190
- research_failed: 171
- proven_liquidity_gone: 63
- simulated failed buy: 51
- proven_low_volume: 6
- research_passed: 1
- proven: 1

Warning: 32 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
