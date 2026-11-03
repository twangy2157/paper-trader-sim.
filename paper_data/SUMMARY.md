# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T22:38:44Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 78.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 374 | 15% | -54.3% | -61 to -48 | -20352 |
| all momentum | 376 | 15% | -54.4% | -61 to -48 | -20492 |
| control | 442 | 8% | -16.4% | -20 to -13 | -7295 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 17 | 35% | -32.9% | -59 to -10 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (355, 15%) | -16% (442, 8%) | -13% (4, 25%) | -33% (17, 35%) |
| wide_sl50_tp100 | -55% (355, 17%) | -17% (442, 8%) | -13% (4, 25%) | -33% (17, 35%) |
| sl30_tp50 | -57% (355, 19%) | -17% (442, 8%) | -22% (4, 25%) | -33% (17, 35%) |
| sl50_tp50 | -56% (355, 21%) | -17% (442, 9%) | -22% (4, 25%) | -33% (17, 35%) |
| no_stop_tp100 | -55% (355, 17%) | -17% (442, 8%) | -13% (4, 25%) | -33% (17, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13842. Outcomes:

- missed_window: 9183
- low_liquidity: 2698
- proven_liquidity_gone: 746
- no_momentum: 497
- research_failed: 381
- simulated failed buy: 146
- proven_low_volume: 139
- proven: 18
- proven_price_collapsed_or_parabolic: 18
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 96 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
