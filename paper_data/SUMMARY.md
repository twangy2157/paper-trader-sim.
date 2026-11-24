# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-24T15:00:05Z. Bankroll cash (research-selected trades): 552.709713614385. Open positions: 14. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 22 | 32% | -20.2% | -49 to 7 | -447 |
| momentum, not picked | 3685 | 12% | -65.8% | -68 to -64 | -242659 |
| all momentum | 3707 | 12% | -65.5% | -67 to -64 | -243106 |
| control | 4449 | 6% | -19.3% | -20 to -18 | -86400 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 132 | 33% | -30.1% | -39 to -21 | -3989 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3686, 12%) | -19% (4449, 6%) | -13% (47, 28%) | -30% (132, 33%) |
| wide_sl50_tp100 | -65% (3686, 13%) | -20% (4449, 6%) | -13% (47, 32%) | -31% (132, 33%) |
| sl30_tp50 | -67% (3686, 14%) | -19% (4449, 7%) | -17% (47, 34%) | -30% (132, 34%) |
| sl50_tp50 | -67% (3686, 15%) | -20% (4449, 8%) | -18% (47, 38%) | -31% (132, 34%) |
| no_stop_tp100 | -65% (3686, 14%) | -20% (4449, 7%) | -12% (47, 32%) | -32% (132, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 120517. Outcomes:

- missed_window: 77869
- low_liquidity: 20608
- proven_liquidity_gone: 10366
- no_momentum: 4502
- research_failed: 3689
- proven_low_volume: 1527
- simulated failed buy: 1522
- proven_price_collapsed_or_parabolic: 167
- proven: 133
- proven_no_uptrend: 65
- dip: 47
- research_passed: 22

Warning: 946 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
