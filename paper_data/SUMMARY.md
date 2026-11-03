# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T17:40:33Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 23. Pools on watchlist: 37.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 339 | 14% | -54.7% | -62 to -48 | -18586 |
| all momentum | 341 | 14% | -54.8% | -61 to -48 | -18726 |
| control | 381 | 8% | -15.9% | -20 to -13 | -6110 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 15 | 33% | -36.8% | -64 to -10 | -553 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (320, 15%) | -16% (381, 8%) | 12% (3, 33%) | -37% (15, 33%) |
| wide_sl50_tp100 | -56% (320, 17%) | -16% (381, 9%) | 12% (3, 33%) | -37% (15, 33%) |
| sl30_tp50 | -57% (320, 19%) | -17% (381, 9%) | 1% (3, 33%) | -37% (15, 33%) |
| sl50_tp50 | -56% (320, 22%) | -17% (381, 9%) | 1% (3, 33%) | -37% (15, 33%) |
| no_stop_tp100 | -56% (320, 17%) | -16% (381, 9%) | 12% (3, 33%) | -37% (15, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12485. Outcomes:

- missed_window: 8272
- low_liquidity: 2510
- proven_liquidity_gone: 639
- no_momentum: 432
- research_failed: 354
- simulated failed buy: 127
- proven_low_volume: 104
- proven_price_collapsed_or_parabolic: 17
- proven: 16
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 83 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
