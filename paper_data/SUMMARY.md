# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-24T10:35:57Z. Bankroll cash (research-selected trades): 463.74568815387. Open positions: 24. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3640 | 12% | -65.8% | -68 to -64 | -239956 |
| all momentum | 3660 | 12% | -65.6% | -67 to -64 | -240392 |
| control | 4407 | 6% | -19.3% | -20 to -18 | -85581 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 132 | 33% | -30.1% | -39 to -21 | -3989 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3639, 12%) | -19% (4407, 6%) | -13% (47, 28%) | -30% (132, 33%) |
| wide_sl50_tp100 | -65% (3639, 13%) | -20% (4407, 6%) | -13% (47, 32%) | -31% (132, 33%) |
| sl30_tp50 | -67% (3639, 14%) | -19% (4407, 7%) | -17% (47, 34%) | -30% (132, 34%) |
| sl50_tp50 | -67% (3639, 15%) | -20% (4407, 8%) | -18% (47, 38%) | -31% (132, 34%) |
| no_stop_tp100 | -65% (3639, 14%) | -20% (4407, 7%) | -12% (47, 32%) | -32% (132, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 119474. Outcomes:

- missed_window: 77242
- low_liquidity: 20399
- proven_liquidity_gone: 10265
- no_momentum: 4463
- research_failed: 3651
- proven_low_volume: 1517
- simulated failed buy: 1507
- proven_price_collapsed_or_parabolic: 166
- proven: 132
- proven_no_uptrend: 64
- dip: 47
- research_passed: 21

Warning: 938 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
