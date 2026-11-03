# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T13:49:10Z. Bankroll cash (research-selected trades): 898.0. Open positions: 21. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 309 | 14% | -54.7% | -61 to -48 | -16923 |
| all momentum | 310 | 14% | -54.8% | -62 to -48 | -17025 |
| control | 342 | 8% | -17.0% | -21 to -13 | -5841 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 12 | 42% | -36.8% | -66 to -7 | -443 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (289, 15%) | -17% (342, 8%) | 24% (2, 50%) | -37% (12, 42%) |
| wide_sl50_tp100 | -56% (289, 17%) | -17% (342, 8%) | 24% (2, 50%) | -37% (12, 42%) |
| sl30_tp50 | -57% (289, 19%) | -18% (342, 8%) | 7% (2, 50%) | -37% (12, 42%) |
| sl50_tp50 | -56% (289, 22%) | -18% (342, 9%) | 7% (2, 50%) | -37% (12, 42%) |
| no_stop_tp100 | -56% (289, 17%) | -17% (342, 8%) | 24% (2, 50%) | -37% (12, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11318. Outcomes:

- missed_window: 7478
- low_liquidity: 2337
- proven_liquidity_gone: 540
- no_momentum: 394
- research_failed: 319
- simulated failed buy: 115
- proven_low_volume: 93
- proven: 15
- proven_price_collapsed_or_parabolic: 15
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 73 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
