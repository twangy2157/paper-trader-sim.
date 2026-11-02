# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T17:45:11Z. Bankroll cash (research-selected trades): 898.5. Open positions: 22. Pools on watchlist: 29.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 166 | 15% | -52.3% | -62 to -43 | -8695 |
| all momentum | 167 | 15% | -52.6% | -61 to -43 | -8796 |
| control | 140 | 11% | -16.0% | -23 to -9 | -2246 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (146, 16%) | -16% (140, 11%) | - | - |
| wide_sl50_tp100 | -55% (146, 18%) | -17% (140, 11%) | - | - |
| sl30_tp50 | -56% (146, 20%) | -18% (140, 11%) | - | - |
| sl50_tp50 | -56% (146, 22%) | -18% (140, 12%) | - | - |
| no_stop_tp100 | -55% (146, 18%) | -17% (140, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5998. Outcomes:

- missed_window: 3947
- low_liquidity: 1533
- no_momentum: 197
- research_failed: 174
- proven_liquidity_gone: 82
- simulated failed buy: 56
- proven_low_volume: 6
- research_passed: 1
- proven: 1
- proven_no_uptrend: 1

Warning: 35 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
