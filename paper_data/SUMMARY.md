# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-24T22:24:43Z. Bankroll cash (research-selected trades): 552.709713614385. Open positions: 11. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 22 | 32% | -20.2% | -49 to 7 | -447 |
| momentum, not picked | 3687 | 12% | -65.8% | -68 to -64 | -242812 |
| all momentum | 3709 | 12% | -65.5% | -67 to -64 | -243259 |
| control | 4456 | 6% | -19.3% | -20 to -18 | -86444 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 133 | 33% | -30.1% | -38 to -21 | -4022 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3688, 12%) | -19% (4456, 6%) | -13% (47, 28%) | -30% (133, 33%) |
| wide_sl50_tp100 | -65% (3688, 13%) | -20% (4456, 7%) | -13% (47, 32%) | -31% (133, 33%) |
| sl30_tp50 | -67% (3688, 14%) | -19% (4456, 7%) | -17% (47, 34%) | -30% (133, 34%) |
| sl50_tp50 | -67% (3688, 15%) | -20% (4456, 8%) | -18% (47, 38%) | -31% (133, 34%) |
| no_stop_tp100 | -65% (3688, 14%) | -20% (4456, 7%) | -12% (47, 32%) | -32% (133, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 120634. Outcomes:

- missed_window: 77954
- low_liquidity: 20625
- proven_liquidity_gone: 10371
- no_momentum: 4508
- research_failed: 3690
- proven_low_volume: 1528
- simulated failed buy: 1524
- proven_price_collapsed_or_parabolic: 167
- proven: 133
- proven_no_uptrend: 65
- dip: 47
- research_passed: 22

Warning: 947 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
