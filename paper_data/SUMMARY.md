# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-22T09:08:09Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 15. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3466 | 12% | -66.1% | -68 to -64 | -229525 |
| all momentum | 3486 | 12% | -65.9% | -68 to -64 | -229962 |
| control | 4204 | 6% | -19.3% | -20 to -18 | -81409 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4017 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3465, 12%) | -19% (4204, 6%) | -13% (47, 28%) | -31% (129, 33%) |
| wide_sl50_tp100 | -66% (3465, 13%) | -20% (4204, 6%) | -13% (47, 32%) | -32% (129, 33%) |
| sl30_tp50 | -68% (3465, 14%) | -19% (4204, 7%) | -17% (47, 34%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3465, 15%) | -20% (4204, 7%) | -18% (47, 38%) | -32% (129, 33%) |
| no_stop_tp100 | -66% (3465, 14%) | -20% (4204, 7%) | -12% (47, 32%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 114479. Outcomes:

- missed_window: 74158
- low_liquidity: 19400
- proven_liquidity_gone: 9869
- no_momentum: 4257
- research_failed: 3472
- proven_low_volume: 1453
- simulated failed buy: 1447
- proven_price_collapsed_or_parabolic: 163
- proven: 129
- proven_no_uptrend: 64
- dip: 47
- research_passed: 20

Warning: 897 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
