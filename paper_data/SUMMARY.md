# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T06:12:39Z. Bankroll cash (research-selected trades): 898.0. Open positions: 23. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 245 | 15% | -51.8% | -60 to -44 | -12704 |
| all momentum | 246 | 15% | -52.0% | -60 to -44 | -12806 |
| control | 273 | 8% | -17.1% | -22 to -13 | -4691 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (225, 16%) | -17% (273, 8%) | 58% (1, 100%) | -100% (4, 0%) |
| wide_sl50_tp100 | -54% (225, 17%) | -18% (273, 8%) | 58% (1, 100%) | -100% (4, 0%) |
| sl30_tp50 | -55% (225, 20%) | -18% (273, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| sl50_tp50 | -54% (225, 22%) | -18% (273, 10%) | 24% (1, 100%) | -100% (4, 0%) |
| no_stop_tp100 | -54% (225, 17%) | -18% (273, 8%) | 58% (1, 100%) | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9507. Outcomes:

- missed_window: 6297
- low_liquidity: 2077
- proven_liquidity_gone: 366
- no_momentum: 330
- research_failed: 253
- simulated failed buy: 94
- proven_low_volume: 64
- proven_price_collapsed_or_parabolic: 10
- proven_no_uptrend: 8
- proven: 6
- research_passed: 1
- dip: 1

Warning: 61 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
