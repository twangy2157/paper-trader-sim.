# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T09:20:35Z. Bankroll cash (research-selected trades): 898.0. Open positions: 34. Pools on watchlist: 86.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 269 | 15% | -52.3% | -60 to -45 | -14091 |
| all momentum | 270 | 15% | -52.5% | -60 to -45 | -14193 |
| control | 297 | 9% | -16.0% | -20 to -12 | -4775 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 6 | 33% | -65.7% | -100 to -31 | -395 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (249, 16%) | -16% (297, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| wide_sl50_tp100 | -54% (249, 17%) | -16% (297, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| sl30_tp50 | -55% (249, 20%) | -17% (297, 9%) | 24% (1, 100%) | -66% (6, 33%) |
| sl50_tp50 | -54% (249, 22%) | -17% (297, 10%) | 24% (1, 100%) | -66% (6, 33%) |
| no_stop_tp100 | -55% (249, 18%) | -16% (297, 9%) | 58% (1, 100%) | -66% (6, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10181. Outcomes:

- missed_window: 6717
- low_liquidity: 2180
- proven_liquidity_gone: 433
- no_momentum: 358
- research_failed: 281
- simulated failed buy: 104
- proven_low_volume: 73
- proven_price_collapsed_or_parabolic: 13
- proven: 11
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 68 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
