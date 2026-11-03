# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T20:32:09Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 17. Pools on watchlist: 28.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 359 | 15% | -53.9% | -60 to -47 | -19371 |
| all momentum | 361 | 15% | -54.0% | -60 to -48 | -19511 |
| control | 417 | 8% | -16.1% | -20 to -13 | -6751 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 16 | 31% | -35.0% | -61 to -11 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (340, 15%) | -16% (417, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| wide_sl50_tp100 | -55% (340, 17%) | -16% (417, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| sl30_tp50 | -56% (340, 19%) | -17% (417, 8%) | 1% (3, 33%) | -35% (16, 31%) |
| sl50_tp50 | -56% (340, 22%) | -17% (417, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| no_stop_tp100 | -55% (340, 18%) | -16% (417, 8%) | 12% (3, 33%) | -35% (16, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13285. Outcomes:

- missed_window: 8826
- low_liquidity: 2606
- proven_liquidity_gone: 700
- no_momentum: 471
- research_failed: 364
- simulated failed buy: 143
- proven_low_volume: 124
- proven: 18
- proven_price_collapsed_or_parabolic: 18
- proven_no_uptrend: 10
- dip: 3
- research_passed: 2

Warning: 94 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
