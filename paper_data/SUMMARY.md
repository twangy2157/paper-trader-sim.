# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T20:46:59Z. Bankroll cash (research-selected trades): 898.5. Open positions: 27. Pools on watchlist: 88.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 183 | 15% | -52.6% | -61 to -43 | -9633 |
| all momentum | 184 | 15% | -52.8% | -61 to -44 | -9735 |
| control | 168 | 11% | -16.0% | -22 to -10 | -2712 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (163, 16%) | -16% (168, 11%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -56% (163, 17%) | -17% (168, 11%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (163, 19%) | -18% (168, 12%) | - | -100% (1, 0%) |
| sl50_tp50 | -56% (163, 21%) | -18% (168, 12%) | - | -100% (1, 0%) |
| no_stop_tp100 | -55% (163, 18%) | -17% (168, 11%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6844. Outcomes:

- missed_window: 4493
- low_liquidity: 1685
- no_momentum: 231
- research_failed: 189
- proven_liquidity_gone: 153
- simulated failed buy: 65
- proven_low_volume: 19
- proven: 3
- proven_price_collapsed_or_parabolic: 3
- proven_no_uptrend: 2
- research_passed: 1

Warning: 43 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
