# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T06:02:34Z. Bankroll cash (research-selected trades): 898.0. Open positions: 26. Pools on watchlist: 33.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 244 | 15% | -51.6% | -59 to -43 | -12604 |
| all momentum | 245 | 15% | -51.8% | -59 to -44 | -12706 |
| control | 268 | 9% | -16.8% | -21 to -12 | -4533 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (224, 16%) | -17% (268, 9%) | 58% (1, 100%) | -100% (4, 0%) |
| wide_sl50_tp100 | -54% (224, 17%) | -17% (268, 9%) | 58% (1, 100%) | -100% (4, 0%) |
| sl30_tp50 | -55% (224, 20%) | -18% (268, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| sl50_tp50 | -54% (224, 22%) | -18% (268, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| no_stop_tp100 | -54% (224, 17%) | -18% (268, 9%) | 58% (1, 100%) | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9474. Outcomes:

- missed_window: 6275
- low_liquidity: 2074
- proven_liquidity_gone: 362
- no_momentum: 328
- research_failed: 252
- simulated failed buy: 94
- proven_low_volume: 64
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 8
- proven: 6
- research_passed: 1
- dip: 1

Warning: 61 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
