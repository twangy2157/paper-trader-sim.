# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-24T12:31:56Z. Bankroll cash (research-selected trades): 554.6729377067182. Open positions: 11. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 21 | 33% | -21.1% | -50 to 9 | -445 |
| momentum, not picked | 3664 | 12% | -65.8% | -68 to -64 | -241423 |
| all momentum | 3685 | 12% | -65.5% | -67 to -64 | -241868 |
| control | 4429 | 6% | -19.3% | -20 to -18 | -86069 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 132 | 33% | -30.1% | -39 to -21 | -3989 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3664, 12%) | -19% (4429, 6%) | -13% (47, 28%) | -30% (132, 33%) |
| wide_sl50_tp100 | -65% (3664, 13%) | -20% (4429, 6%) | -13% (47, 32%) | -31% (132, 33%) |
| sl30_tp50 | -67% (3664, 14%) | -19% (4429, 7%) | -17% (47, 34%) | -30% (132, 34%) |
| sl50_tp50 | -67% (3664, 15%) | -20% (4429, 8%) | -18% (47, 38%) | -31% (132, 34%) |
| no_stop_tp100 | -65% (3664, 14%) | -20% (4429, 7%) | -12% (47, 32%) | -32% (132, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 119896. Outcomes:

- missed_window: 77502
- low_liquidity: 20480
- proven_liquidity_gone: 10303
- no_momentum: 4476
- research_failed: 3672
- proven_low_volume: 1520
- simulated failed buy: 1513
- proven_price_collapsed_or_parabolic: 166
- proven: 132
- proven_no_uptrend: 64
- dip: 47
- research_passed: 21

Warning: 940 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
