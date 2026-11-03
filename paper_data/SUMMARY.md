# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T13:27:34Z. Bankroll cash (research-selected trades): 898.0. Open positions: 14. Pools on watchlist: 75.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 306 | 14% | -54.3% | -61 to -47 | -16631 |
| all momentum | 307 | 14% | -54.4% | -61 to -47 | -16733 |
| control | 342 | 8% | -17.0% | -21 to -13 | -5841 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 12 | 42% | -36.8% | -66 to -7 | -443 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (286, 15%) | -17% (342, 8%) | 24% (2, 50%) | -37% (12, 42%) |
| wide_sl50_tp100 | -56% (286, 17%) | -17% (342, 8%) | 24% (2, 50%) | -37% (12, 42%) |
| sl30_tp50 | -57% (286, 19%) | -18% (342, 8%) | 7% (2, 50%) | -37% (12, 42%) |
| sl50_tp50 | -56% (286, 22%) | -18% (342, 9%) | 7% (2, 50%) | -37% (12, 42%) |
| no_stop_tp100 | -56% (286, 17%) | -17% (342, 8%) | 24% (2, 50%) | -37% (12, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11206. Outcomes:

- missed_window: 7404
- low_liquidity: 2322
- proven_liquidity_gone: 530
- no_momentum: 389
- research_failed: 314
- simulated failed buy: 114
- proven_low_volume: 92
- proven: 15
- proven_price_collapsed_or_parabolic: 14
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 73 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
