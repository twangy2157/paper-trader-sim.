# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T16:35:00Z. Bankroll cash (research-selected trades): 572.1048725040199. Open positions: 17. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 13 | 23% | -32.8% | -65 to 3 | -428 |
| momentum, not picked | 1015 | 13% | -61.0% | -65 to -57 | -62018 |
| all momentum | 1028 | 13% | -60.6% | -64 to -57 | -62446 |
| control | 1296 | 6% | -19.9% | -22 to -18 | -25923 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 52 | 48% | -15.9% | -30 to -3 | -832 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1007, 13%) | -20% (1296, 6%) | -40% (10, 10%) | -16% (52, 48%) |
| wide_sl50_tp100 | -61% (1007, 15%) | -20% (1296, 7%) | -43% (10, 10%) | -16% (52, 48%) |
| sl30_tp50 | -62% (1007, 16%) | -20% (1296, 7%) | -44% (10, 10%) | -18% (52, 48%) |
| sl50_tp50 | -62% (1007, 18%) | -20% (1296, 7%) | -47% (10, 10%) | -18% (52, 48%) |
| no_stop_tp100 | -61% (1007, 16%) | -21% (1296, 7%) | -40% (10, 10%) | -16% (52, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 36040. Outcomes:

- missed_window: 23341
- low_liquidity: 6505
- proven_liquidity_gone: 2817
- no_momentum: 1346
- research_failed: 1025
- simulated failed buy: 445
- proven_low_volume: 401
- proven_price_collapsed_or_parabolic: 60
- proven: 53
- proven_no_uptrend: 24
- research_passed: 13
- dip: 10

Warning: 280 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
