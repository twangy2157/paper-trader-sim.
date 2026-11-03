# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T09:53:00Z. Bankroll cash (research-selected trades): 898.0. Open positions: 23. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 279 | 15% | -53.0% | -61 to -46 | -14821 |
| all momentum | 280 | 15% | -53.2% | -61 to -45 | -14923 |
| control | 303 | 9% | -16.1% | -20 to -12 | -4913 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 7 | 29% | -56.9% | -87 to -14 | -399 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (259, 16%) | -16% (303, 9%) | 58% (1, 100%) | -57% (7, 29%) |
| wide_sl50_tp100 | -55% (259, 17%) | -17% (303, 9%) | 58% (1, 100%) | -57% (7, 29%) |
| sl30_tp50 | -56% (259, 20%) | -17% (303, 9%) | 24% (1, 100%) | -57% (7, 29%) |
| sl50_tp50 | -55% (259, 22%) | -17% (303, 10%) | 24% (1, 100%) | -57% (7, 29%) |
| no_stop_tp100 | -55% (259, 18%) | -17% (303, 9%) | 58% (1, 100%) | -57% (7, 29%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10350. Outcomes:

- missed_window: 6845
- low_liquidity: 2194
- proven_liquidity_gone: 449
- no_momentum: 362
- research_failed: 283
- simulated failed buy: 107
- proven_low_volume: 75
- proven_price_collapsed_or_parabolic: 13
- proven: 11
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 69 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
