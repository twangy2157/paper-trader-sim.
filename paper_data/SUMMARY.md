# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T18:12:29Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 18. Pools on watchlist: 79.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 347 | 15% | -53.6% | -60 to -47 | -18620 |
| all momentum | 349 | 15% | -53.7% | -60 to -47 | -18760 |
| control | 385 | 8% | -16.4% | -20 to -13 | -6333 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 15 | 33% | -36.8% | -64 to -10 | -553 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (328, 15%) | -16% (385, 8%) | 12% (3, 33%) | -37% (15, 33%) |
| wide_sl50_tp100 | -55% (328, 17%) | -17% (385, 9%) | 12% (3, 33%) | -37% (15, 33%) |
| sl30_tp50 | -56% (328, 20%) | -17% (385, 9%) | 1% (3, 33%) | -37% (15, 33%) |
| sl50_tp50 | -55% (328, 22%) | -17% (385, 9%) | 1% (3, 33%) | -37% (15, 33%) |
| no_stop_tp100 | -55% (328, 18%) | -17% (385, 9%) | 12% (3, 33%) | -37% (15, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12625. Outcomes:

- missed_window: 8364
- low_liquidity: 2532
- proven_liquidity_gone: 653
- no_momentum: 436
- research_failed: 357
- simulated failed buy: 129
- proven_low_volume: 107
- proven_price_collapsed_or_parabolic: 17
- proven: 16
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 84 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
