# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T14:59:29Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 17. Pools on watchlist: 83.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 1005 | 13% | -61.1% | -65 to -57 | -61525 |
| all momentum | 1017 | 13% | -60.8% | -65 to -57 | -61920 |
| control | 1281 | 6% | -20.1% | -22 to -18 | -25824 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 52 | 48% | -15.9% | -30 to -3 | -832 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (996, 13%) | -20% (1281, 6%) | -40% (10, 10%) | -16% (52, 48%) |
| wide_sl50_tp100 | -61% (996, 15%) | -20% (1281, 7%) | -43% (10, 10%) | -16% (52, 48%) |
| sl30_tp50 | -62% (996, 16%) | -20% (1281, 7%) | -44% (10, 10%) | -18% (52, 48%) |
| sl50_tp50 | -62% (996, 18%) | -21% (1281, 7%) | -47% (10, 10%) | -18% (52, 48%) |
| no_stop_tp100 | -61% (996, 16%) | -21% (1281, 7%) | -40% (10, 10%) | -16% (52, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 35527. Outcomes:

- missed_window: 22988
- low_liquidity: 6426
- proven_liquidity_gone: 2779
- no_momentum: 1336
- research_failed: 1010
- simulated failed buy: 438
- proven_low_volume: 393
- proven_price_collapsed_or_parabolic: 58
- proven: 53
- proven_no_uptrend: 24
- research_passed: 12
- dip: 10

Warning: 276 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
