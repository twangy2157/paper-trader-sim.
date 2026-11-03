# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T23:00:57Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 14. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 377 | 15% | -54.4% | -61 to -48 | -20559 |
| all momentum | 379 | 15% | -54.5% | -61 to -48 | -20699 |
| control | 448 | 8% | -16.3% | -20 to -13 | -7344 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 17 | 35% | -32.9% | -59 to -10 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (358, 15%) | -16% (448, 8%) | -13% (4, 25%) | -33% (17, 35%) |
| wide_sl50_tp100 | -56% (358, 17%) | -17% (448, 8%) | -13% (4, 25%) | -33% (17, 35%) |
| sl30_tp50 | -57% (358, 19%) | -17% (448, 8%) | -22% (4, 25%) | -33% (17, 35%) |
| sl50_tp50 | -56% (358, 21%) | -17% (448, 8%) | -22% (4, 25%) | -33% (17, 35%) |
| no_stop_tp100 | -56% (358, 17%) | -17% (448, 8%) | -13% (4, 25%) | -33% (17, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13973. Outcomes:

- missed_window: 9284
- low_liquidity: 2714
- proven_liquidity_gone: 754
- no_momentum: 499
- research_failed: 382
- simulated failed buy: 147
- proven_low_volume: 139
- proven: 19
- proven_price_collapsed_or_parabolic: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 97 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
