# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-24T11:39:13Z. Bankroll cash (research-selected trades): 554.6729377067182. Open positions: 23. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 21 | 33% | -21.1% | -50 to 9 | -445 |
| momentum, not picked | 3651 | 12% | -65.8% | -68 to -64 | -240444 |
| all momentum | 3672 | 12% | -65.5% | -67 to -64 | -240889 |
| control | 4419 | 6% | -19.3% | -20 to -18 | -85824 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 132 | 33% | -30.1% | -39 to -21 | -3989 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3651, 12%) | -19% (4419, 6%) | -13% (47, 28%) | -30% (132, 33%) |
| wide_sl50_tp100 | -65% (3651, 13%) | -20% (4419, 6%) | -13% (47, 32%) | -31% (132, 33%) |
| sl30_tp50 | -67% (3651, 14%) | -19% (4419, 7%) | -17% (47, 34%) | -30% (132, 34%) |
| sl50_tp50 | -67% (3651, 15%) | -20% (4419, 8%) | -18% (47, 38%) | -31% (132, 34%) |
| no_stop_tp100 | -65% (3651, 14%) | -20% (4419, 7%) | -12% (47, 32%) | -32% (132, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 119675. Outcomes:

- missed_window: 77353
- low_liquidity: 20455
- proven_liquidity_gone: 10271
- no_momentum: 4473
- research_failed: 3664
- proven_low_volume: 1517
- simulated failed buy: 1512
- proven_price_collapsed_or_parabolic: 166
- proven: 132
- proven_no_uptrend: 64
- dip: 47
- research_passed: 21

Warning: 940 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
