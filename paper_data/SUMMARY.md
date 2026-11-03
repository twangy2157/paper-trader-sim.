# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T21:47:40Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 29. Pools on watchlist: 73.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 366 | 14% | -54.2% | -61 to -48 | -19883 |
| all momentum | 368 | 14% | -54.3% | -61 to -48 | -20023 |
| control | 429 | 8% | -15.8% | -19 to -13 | -6822 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 16 | 31% | -35.0% | -61 to -11 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (347, 15%) | -16% (429, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| wide_sl50_tp100 | -55% (347, 17%) | -16% (429, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| sl30_tp50 | -57% (347, 19%) | -17% (429, 8%) | 1% (3, 33%) | -35% (16, 31%) |
| sl50_tp50 | -56% (347, 21%) | -17% (429, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| no_stop_tp100 | -55% (347, 17%) | -16% (429, 8%) | 12% (3, 33%) | -35% (16, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13598. Outcomes:

- missed_window: 9013
- low_liquidity: 2663
- proven_liquidity_gone: 725
- no_momentum: 490
- research_failed: 375
- simulated failed buy: 144
- proven_low_volume: 136
- proven: 18
- proven_price_collapsed_or_parabolic: 18
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 94 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
