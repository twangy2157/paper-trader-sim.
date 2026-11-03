# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T13:37:41Z. Bankroll cash (research-selected trades): 898.0. Open positions: 15. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 308 | 14% | -54.5% | -62 to -47 | -16823 |
| all momentum | 309 | 14% | -54.7% | -61 to -47 | -16925 |
| control | 342 | 8% | -17.0% | -21 to -13 | -5841 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 12 | 42% | -36.8% | -66 to -7 | -443 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (288, 15%) | -17% (342, 8%) | 24% (2, 50%) | -37% (12, 42%) |
| wide_sl50_tp100 | -56% (288, 17%) | -17% (342, 8%) | 24% (2, 50%) | -37% (12, 42%) |
| sl30_tp50 | -57% (288, 19%) | -18% (342, 8%) | 7% (2, 50%) | -37% (12, 42%) |
| sl50_tp50 | -56% (288, 22%) | -18% (342, 9%) | 7% (2, 50%) | -37% (12, 42%) |
| no_stop_tp100 | -56% (288, 17%) | -17% (342, 8%) | 24% (2, 50%) | -37% (12, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11271. Outcomes:

- missed_window: 7452
- low_liquidity: 2330
- proven_liquidity_gone: 534
- no_momentum: 391
- research_failed: 315
- simulated failed buy: 115
- proven_low_volume: 93
- proven: 15
- proven_price_collapsed_or_parabolic: 14
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 73 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
