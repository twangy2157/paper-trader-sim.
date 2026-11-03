# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T05:08:31Z. Bankroll cash (research-selected trades): 898.0. Open positions: 21. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 234 | 15% | -51.4% | -59 to -43 | -12059 |
| all momentum | 235 | 15% | -51.6% | -59 to -44 | -12161 |
| control | 265 | 9% | -16.6% | -21 to -12 | -4414 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (214, 16%) | -17% (265, 9%) | 58% (1, 100%) | -100% (4, 0%) |
| wide_sl50_tp100 | -54% (214, 17%) | -17% (265, 9%) | 58% (1, 100%) | -100% (4, 0%) |
| sl30_tp50 | -55% (214, 20%) | -18% (265, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| sl50_tp50 | -55% (214, 21%) | -18% (265, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| no_stop_tp100 | -54% (214, 18%) | -17% (265, 9%) | 58% (1, 100%) | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9221. Outcomes:

- missed_window: 6120
- low_liquidity: 2025
- proven_liquidity_gone: 335
- no_momentum: 317
- research_failed: 245
- simulated failed buy: 93
- proven_low_volume: 62
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 7
- proven: 6
- research_passed: 1
- dip: 1

Warning: 60 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
