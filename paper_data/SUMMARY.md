# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T21:58:00Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 29. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 367 | 15% | -54.0% | -60 to -47 | -19847 |
| all momentum | 369 | 15% | -54.1% | -61 to -48 | -19987 |
| control | 430 | 8% | -15.8% | -19 to -13 | -6825 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 17 | 35% | -32.9% | -59 to -10 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (348, 15%) | -16% (430, 8%) | 12% (3, 33%) | -33% (17, 35%) |
| wide_sl50_tp100 | -55% (348, 17%) | -16% (430, 8%) | 12% (3, 33%) | -33% (17, 35%) |
| sl30_tp50 | -57% (348, 19%) | -17% (430, 8%) | 1% (3, 33%) | -33% (17, 35%) |
| sl50_tp50 | -56% (348, 22%) | -17% (430, 9%) | 1% (3, 33%) | -33% (17, 35%) |
| no_stop_tp100 | -55% (348, 18%) | -16% (430, 8%) | 12% (3, 33%) | -33% (17, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13655. Outcomes:

- missed_window: 9053
- low_liquidity: 2672
- proven_liquidity_gone: 730
- no_momentum: 491
- research_failed: 377
- simulated failed buy: 144
- proven_low_volume: 136
- proven: 18
- proven_price_collapsed_or_parabolic: 18
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 94 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
