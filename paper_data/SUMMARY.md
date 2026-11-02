# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T18:28:30Z. Bankroll cash (research-selected trades): 898.5. Open positions: 17. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 173 | 15% | -52.1% | -61 to -43 | -9029 |
| all momentum | 174 | 15% | -52.4% | -61 to -43 | -9130 |
| control | 147 | 12% | -14.8% | -21 to -8 | -2186 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (153, 16%) | -15% (147, 12%) | - | - |
| wide_sl50_tp100 | -55% (153, 18%) | -16% (147, 12%) | - | - |
| sl30_tp50 | -56% (153, 20%) | -17% (147, 12%) | - | - |
| sl50_tp50 | -55% (153, 22%) | -17% (147, 13%) | - | - |
| no_stop_tp100 | -54% (153, 18%) | -16% (147, 12%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6254. Outcomes:

- missed_window: 4129
- low_liquidity: 1568
- no_momentum: 204
- research_failed: 176
- proven_liquidity_gone: 107
- simulated failed buy: 57
- proven_low_volume: 9
- proven_no_uptrend: 2
- research_passed: 1
- proven: 1

Warning: 36 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
