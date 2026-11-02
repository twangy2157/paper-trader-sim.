# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T21:40:43Z. Bankroll cash (research-selected trades): 898.5. Open positions: 23. Pools on watchlist: 77.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 189 | 15% | -52.0% | -61 to -43 | -9852 |
| all momentum | 190 | 15% | -52.3% | -61 to -44 | -9953 |
| control | 184 | 10% | -16.3% | -22 to -11 | -3024 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (169, 16%) | -16% (184, 10%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -55% (169, 17%) | -17% (184, 10%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (169, 20%) | -18% (184, 11%) | - | -100% (1, 0%) |
| sl50_tp50 | -55% (169, 22%) | -18% (184, 11%) | - | -100% (1, 0%) |
| no_stop_tp100 | -54% (169, 18%) | -17% (184, 10%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7188. Outcomes:

- missed_window: 4764
- low_liquidity: 1715
- no_momentum: 243
- research_failed: 195
- proven_liquidity_gone: 170
- simulated failed buy: 68
- proven_low_volume: 21
- proven_no_uptrend: 4
- proven_price_collapsed_or_parabolic: 4
- proven: 3
- research_passed: 1

Warning: 46 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
