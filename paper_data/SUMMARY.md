# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T21:15:39Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 22. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 362 | 15% | -54.3% | -61 to -48 | -19673 |
| all momentum | 364 | 15% | -54.3% | -60 to -48 | -19812 |
| control | 426 | 8% | -15.9% | -19 to -13 | -6804 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 16 | 31% | -35.0% | -61 to -11 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (343, 15%) | -16% (426, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| wide_sl50_tp100 | -55% (343, 17%) | -16% (426, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| sl30_tp50 | -57% (343, 19%) | -17% (426, 8%) | 1% (3, 33%) | -35% (16, 31%) |
| sl50_tp50 | -56% (343, 22%) | -17% (426, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| no_stop_tp100 | -55% (343, 17%) | -16% (426, 8%) | 12% (3, 33%) | -35% (16, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13433. Outcomes:

- missed_window: 8907
- low_liquidity: 2638
- proven_liquidity_gone: 709
- no_momentum: 480
- research_failed: 372
- simulated failed buy: 143
- proven_low_volume: 133
- proven: 18
- proven_price_collapsed_or_parabolic: 18
- proven_no_uptrend: 10
- dip: 3
- research_passed: 2

Warning: 94 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
