# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-24T11:28:38Z. Bankroll cash (research-selected trades): 463.74568815387. Open positions: 29. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3648 | 12% | -65.7% | -68 to -64 | -240143 |
| all momentum | 3668 | 12% | -65.5% | -67 to -64 | -240579 |
| control | 4416 | 6% | -19.3% | -20 to -18 | -85768 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 132 | 33% | -30.1% | -39 to -21 | -3989 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3647, 12%) | -19% (4416, 6%) | -13% (47, 28%) | -30% (132, 33%) |
| wide_sl50_tp100 | -65% (3647, 13%) | -20% (4416, 6%) | -13% (47, 32%) | -31% (132, 33%) |
| sl30_tp50 | -67% (3647, 14%) | -19% (4416, 7%) | -17% (47, 34%) | -30% (132, 34%) |
| sl50_tp50 | -67% (3647, 15%) | -20% (4416, 8%) | -18% (47, 38%) | -31% (132, 34%) |
| no_stop_tp100 | -65% (3647, 14%) | -20% (4416, 7%) | -12% (47, 32%) | -32% (132, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 119641. Outcomes:

- missed_window: 77329
- low_liquidity: 20452
- proven_liquidity_gone: 10265
- no_momentum: 4473
- research_failed: 3663
- proven_low_volume: 1517
- simulated failed buy: 1512
- proven_price_collapsed_or_parabolic: 166
- proven: 132
- proven_no_uptrend: 64
- dip: 47
- research_passed: 21

Warning: 940 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
