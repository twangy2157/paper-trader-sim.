# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T19:39:33Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 27. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 357 | 15% | -53.8% | -61 to -47 | -19253 |
| all momentum | 359 | 15% | -53.9% | -60 to -48 | -19392 |
| control | 400 | 8% | -16.0% | -20 to -13 | -6454 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 16 | 31% | -35.0% | -61 to -11 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (338, 15%) | -16% (400, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| wide_sl50_tp100 | -55% (338, 17%) | -16% (400, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| sl30_tp50 | -56% (338, 20%) | -17% (400, 8%) | 1% (3, 33%) | -35% (16, 31%) |
| sl50_tp50 | -56% (338, 22%) | -17% (400, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| no_stop_tp100 | -55% (338, 18%) | -16% (400, 8%) | 12% (3, 33%) | -35% (16, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13034. Outcomes:

- missed_window: 8655
- low_liquidity: 2568
- proven_liquidity_gone: 685
- no_momentum: 467
- research_failed: 360
- simulated failed buy: 135
- proven_low_volume: 115
- proven: 17
- proven_price_collapsed_or_parabolic: 17
- proven_no_uptrend: 10
- dip: 3
- research_passed: 2

Warning: 89 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
