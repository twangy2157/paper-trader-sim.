# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T10:04:31Z. Bankroll cash (research-selected trades): 898.0. Open positions: 23. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 280 | 15% | -53.2% | -61 to -46 | -14921 |
| all momentum | 281 | 15% | -53.4% | -61 to -46 | -15023 |
| control | 305 | 9% | -16.1% | -20 to -12 | -4932 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 7 | 29% | -56.9% | -87 to -14 | -399 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (260, 16%) | -16% (305, 9%) | 58% (1, 100%) | -57% (7, 29%) |
| wide_sl50_tp100 | -55% (260, 17%) | -17% (305, 9%) | 58% (1, 100%) | -57% (7, 29%) |
| sl30_tp50 | -56% (260, 20%) | -17% (305, 9%) | 24% (1, 100%) | -57% (7, 29%) |
| sl50_tp50 | -56% (260, 22%) | -17% (305, 10%) | 24% (1, 100%) | -57% (7, 29%) |
| no_stop_tp100 | -55% (260, 18%) | -17% (305, 9%) | 58% (1, 100%) | -57% (7, 29%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10408. Outcomes:

- missed_window: 6883
- low_liquidity: 2203
- proven_liquidity_gone: 457
- no_momentum: 365
- research_failed: 283
- simulated failed buy: 107
- proven_low_volume: 75
- proven_price_collapsed_or_parabolic: 13
- proven: 11
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 69 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
