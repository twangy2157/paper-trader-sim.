# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T15:53:00Z. Bankroll cash (research-selected trades): 505.1869477321155. Open positions: 21. Pools on watchlist: 81.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 1008 | 13% | -61.1% | -65 to -58 | -61693 |
| all momentum | 1020 | 13% | -60.8% | -64 to -57 | -62088 |
| control | 1291 | 6% | -20.0% | -22 to -18 | -25897 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 52 | 48% | -15.9% | -30 to -3 | -832 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (999, 13%) | -20% (1291, 6%) | -40% (10, 10%) | -16% (52, 48%) |
| wide_sl50_tp100 | -61% (999, 15%) | -20% (1291, 7%) | -43% (10, 10%) | -16% (52, 48%) |
| sl30_tp50 | -62% (999, 16%) | -20% (1291, 7%) | -44% (10, 10%) | -18% (52, 48%) |
| sl50_tp50 | -62% (999, 18%) | -21% (1291, 7%) | -47% (10, 10%) | -18% (52, 48%) |
| no_stop_tp100 | -61% (999, 16%) | -21% (1291, 7%) | -40% (10, 10%) | -16% (52, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 35790. Outcomes:

- missed_window: 23162
- low_liquidity: 6465
- proven_liquidity_gone: 2800
- no_momentum: 1342
- research_failed: 1020
- simulated failed buy: 445
- proven_low_volume: 396
- proven_price_collapsed_or_parabolic: 60
- proven: 53
- proven_no_uptrend: 24
- research_passed: 13
- dip: 10

Warning: 280 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
