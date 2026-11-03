# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T06:23:56Z. Bankroll cash (research-selected trades): 898.0. Open positions: 21. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 247 | 15% | -51.7% | -59 to -43 | -12792 |
| all momentum | 248 | 15% | -51.9% | -60 to -44 | -12894 |
| control | 275 | 8% | -17.0% | -22 to -12 | -4699 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (227, 16%) | -17% (275, 8%) | 58% (1, 100%) | -100% (4, 0%) |
| wide_sl50_tp100 | -54% (227, 17%) | -17% (275, 8%) | 58% (1, 100%) | -100% (4, 0%) |
| sl30_tp50 | -54% (227, 20%) | -18% (275, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| sl50_tp50 | -53% (227, 22%) | -18% (275, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| no_stop_tp100 | -54% (227, 18%) | -18% (275, 8%) | 58% (1, 100%) | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9551. Outcomes:

- missed_window: 6325
- low_liquidity: 2085
- proven_liquidity_gone: 371
- no_momentum: 330
- research_failed: 254
- simulated failed buy: 94
- proven_low_volume: 64
- proven_price_collapsed_or_parabolic: 11
- proven_no_uptrend: 8
- proven: 7
- research_passed: 1
- dip: 1

Warning: 61 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
