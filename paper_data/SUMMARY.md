# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-24T13:24:37Z. Bankroll cash (research-selected trades): 554.6729377067182. Open positions: 25. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 21 | 33% | -21.1% | -50 to 9 | -445 |
| momentum, not picked | 3670 | 12% | -65.7% | -68 to -64 | -241602 |
| all momentum | 3691 | 12% | -65.5% | -67 to -64 | -242047 |
| control | 4431 | 6% | -19.3% | -20 to -18 | -85988 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 132 | 33% | -30.1% | -39 to -21 | -3989 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3670, 12%) | -19% (4431, 6%) | -13% (47, 28%) | -30% (132, 33%) |
| wide_sl50_tp100 | -65% (3670, 13%) | -20% (4431, 6%) | -13% (47, 32%) | -31% (132, 33%) |
| sl30_tp50 | -67% (3670, 14%) | -19% (4431, 7%) | -17% (47, 34%) | -30% (132, 34%) |
| sl50_tp50 | -67% (3670, 15%) | -20% (4431, 8%) | -18% (47, 38%) | -31% (132, 34%) |
| no_stop_tp100 | -65% (3670, 14%) | -20% (4431, 7%) | -12% (47, 32%) | -32% (132, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 120090. Outcomes:

- missed_window: 77594
- low_liquidity: 20539
- proven_liquidity_gone: 10321
- no_momentum: 4489
- research_failed: 3681
- proven_low_volume: 1521
- simulated failed buy: 1515
- proven_price_collapsed_or_parabolic: 166
- proven: 132
- proven_no_uptrend: 64
- dip: 47
- research_passed: 21

Warning: 942 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
