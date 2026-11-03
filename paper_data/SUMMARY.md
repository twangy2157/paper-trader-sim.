# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T20:21:39Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 17. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 358 | 15% | -53.7% | -60 to -47 | -19271 |
| all momentum | 360 | 15% | -53.8% | -60 to -47 | -19411 |
| control | 415 | 8% | -16.1% | -19 to -13 | -6723 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 16 | 31% | -35.0% | -61 to -11 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (339, 15%) | -16% (415, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| wide_sl50_tp100 | -55% (339, 17%) | -16% (415, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| sl30_tp50 | -56% (339, 19%) | -17% (415, 8%) | 1% (3, 33%) | -35% (16, 31%) |
| sl50_tp50 | -56% (339, 22%) | -17% (415, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| no_stop_tp100 | -55% (339, 18%) | -16% (415, 8%) | 12% (3, 33%) | -35% (16, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13237. Outcomes:

- missed_window: 8794
- low_liquidity: 2599
- proven_liquidity_gone: 698
- no_momentum: 470
- research_failed: 362
- simulated failed buy: 142
- proven_low_volume: 122
- proven: 18
- proven_price_collapsed_or_parabolic: 17
- proven_no_uptrend: 10
- dip: 3
- research_passed: 2

Warning: 94 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
