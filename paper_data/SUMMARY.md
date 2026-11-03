# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T10:15:42Z. Bankroll cash (research-selected trades): 898.0. Open positions: 19. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 281 | 15% | -53.0% | -60 to -45 | -14926 |
| all momentum | 282 | 15% | -53.2% | -61 to -46 | -15028 |
| control | 311 | 8% | -15.9% | -20 to -12 | -4985 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 7 | 29% | -56.9% | -87 to -14 | -399 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (261, 16%) | -16% (311, 8%) | 58% (1, 100%) | -57% (7, 29%) |
| wide_sl50_tp100 | -55% (261, 17%) | -16% (311, 8%) | 58% (1, 100%) | -57% (7, 29%) |
| sl30_tp50 | -56% (261, 20%) | -17% (311, 9%) | 24% (1, 100%) | -57% (7, 29%) |
| sl50_tp50 | -55% (261, 22%) | -17% (311, 9%) | 24% (1, 100%) | -57% (7, 29%) |
| no_stop_tp100 | -55% (261, 18%) | -16% (311, 8%) | 58% (1, 100%) | -57% (7, 29%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10454. Outcomes:

- missed_window: 6916
- low_liquidity: 2205
- proven_liquidity_gone: 462
- no_momentum: 368
- research_failed: 283
- simulated failed buy: 108
- proven_low_volume: 77
- proven_price_collapsed_or_parabolic: 13
- proven: 11
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 70 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
