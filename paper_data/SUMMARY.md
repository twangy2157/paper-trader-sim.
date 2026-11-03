# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T22:28:36Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 373 | 15% | -54.2% | -60 to -48 | -20252 |
| all momentum | 375 | 15% | -54.3% | -61 to -48 | -20392 |
| control | 440 | 8% | -16.5% | -20 to -13 | -7286 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 17 | 35% | -32.9% | -59 to -10 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (354, 15%) | -16% (440, 8%) | 12% (3, 33%) | -33% (17, 35%) |
| wide_sl50_tp100 | -55% (354, 17%) | -17% (440, 8%) | 12% (3, 33%) | -33% (17, 35%) |
| sl30_tp50 | -57% (354, 19%) | -17% (440, 8%) | 1% (3, 33%) | -33% (17, 35%) |
| sl50_tp50 | -56% (354, 21%) | -17% (440, 8%) | 1% (3, 33%) | -33% (17, 35%) |
| no_stop_tp100 | -55% (354, 18%) | -17% (440, 8%) | 12% (3, 33%) | -33% (17, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13794. Outcomes:

- missed_window: 9148
- low_liquidity: 2691
- proven_liquidity_gone: 744
- no_momentum: 496
- research_failed: 378
- simulated failed buy: 146
- proven_low_volume: 139
- proven: 18
- proven_price_collapsed_or_parabolic: 18
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 96 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
