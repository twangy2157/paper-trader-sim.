# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T22:18:29Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 24. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 372 | 15% | -54.1% | -60 to -47 | -20152 |
| all momentum | 374 | 15% | -54.2% | -60 to -48 | -20292 |
| control | 435 | 8% | -16.0% | -19 to -13 | -6995 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 17 | 35% | -32.9% | -59 to -10 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (353, 15%) | -16% (435, 8%) | 12% (3, 33%) | -33% (17, 35%) |
| wide_sl50_tp100 | -55% (353, 17%) | -16% (435, 8%) | 12% (3, 33%) | -33% (17, 35%) |
| sl30_tp50 | -57% (353, 19%) | -17% (435, 8%) | 1% (3, 33%) | -33% (17, 35%) |
| sl50_tp50 | -56% (353, 22%) | -17% (435, 9%) | 1% (3, 33%) | -33% (17, 35%) |
| no_stop_tp100 | -55% (353, 18%) | -16% (435, 8%) | 12% (3, 33%) | -33% (17, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13742. Outcomes:

- missed_window: 9109
- low_liquidity: 2685
- proven_liquidity_gone: 739
- no_momentum: 495
- research_failed: 378
- simulated failed buy: 146
- proven_low_volume: 138
- proven: 18
- proven_price_collapsed_or_parabolic: 18
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 96 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
