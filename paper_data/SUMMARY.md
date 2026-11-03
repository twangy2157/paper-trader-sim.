# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T17:18:44Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 337 | 14% | -55.0% | -61 to -48 | -18577 |
| all momentum | 339 | 14% | -55.1% | -62 to -48 | -18717 |
| control | 381 | 8% | -15.9% | -20 to -13 | -6110 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 15 | 33% | -36.8% | -64 to -10 | -553 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (318, 14%) | -16% (381, 8%) | 12% (3, 33%) | -37% (15, 33%) |
| wide_sl50_tp100 | -56% (318, 16%) | -16% (381, 9%) | 12% (3, 33%) | -37% (15, 33%) |
| sl30_tp50 | -57% (318, 19%) | -17% (381, 9%) | 1% (3, 33%) | -37% (15, 33%) |
| sl50_tp50 | -56% (318, 21%) | -17% (381, 9%) | 1% (3, 33%) | -37% (15, 33%) |
| no_stop_tp100 | -56% (318, 17%) | -16% (381, 9%) | 12% (3, 33%) | -37% (15, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12401. Outcomes:

- missed_window: 8232
- low_liquidity: 2485
- proven_liquidity_gone: 630
- no_momentum: 431
- research_failed: 349
- simulated failed buy: 125
- proven_low_volume: 102
- proven_price_collapsed_or_parabolic: 17
- proven: 16
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 82 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
