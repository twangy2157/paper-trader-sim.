# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T16:52:43Z. Bankroll cash (research-selected trades): 898.5. Open positions: 23. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 153 | 15% | -51.7% | -61 to -41 | -7923 |
| all momentum | 154 | 15% | -52.0% | -62 to -42 | -8024 |
| control | 135 | 11% | -15.0% | -22 to -8 | -2035 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (133, 17%) | -15% (135, 11%) | - | - |
| wide_sl50_tp100 | -55% (133, 18%) | -16% (135, 11%) | - | - |
| sl30_tp50 | -55% (133, 20%) | -17% (135, 12%) | - | - |
| sl50_tp50 | -55% (133, 23%) | -17% (135, 13%) | - | - |
| no_stop_tp100 | -56% (133, 18%) | -16% (135, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5732. Outcomes:

- missed_window: 3767
- low_liquidity: 1498
- no_momentum: 186
- research_failed: 169
- proven_liquidity_gone: 54
- simulated failed buy: 51
- proven_low_volume: 6
- research_passed: 1

Warning: 32 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
