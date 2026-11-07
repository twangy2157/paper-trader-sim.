# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T16:45:10Z. Bankroll cash (research-selected trades): 472.1048725040199. Open positions: 18. Pools on watchlist: 78.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 13 | 23% | -32.8% | -65 to 3 | -428 |
| momentum, not picked | 1019 | 13% | -61.1% | -65 to -57 | -62363 |
| all momentum | 1032 | 13% | -60.7% | -64 to -57 | -62791 |
| control | 1297 | 6% | -19.9% | -22 to -18 | -25929 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 52 | 48% | -15.9% | -30 to -3 | -832 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1011, 13%) | -20% (1297, 6%) | -40% (10, 10%) | -16% (52, 48%) |
| wide_sl50_tp100 | -61% (1011, 15%) | -20% (1297, 7%) | -43% (10, 10%) | -16% (52, 48%) |
| sl30_tp50 | -62% (1011, 16%) | -20% (1297, 7%) | -44% (10, 10%) | -18% (52, 48%) |
| sl50_tp50 | -62% (1011, 18%) | -20% (1297, 7%) | -47% (10, 10%) | -18% (52, 48%) |
| no_stop_tp100 | -61% (1011, 16%) | -21% (1297, 7%) | -40% (10, 10%) | -16% (52, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 36087. Outcomes:

- missed_window: 23377
- low_liquidity: 6508
- proven_liquidity_gone: 2819
- no_momentum: 1349
- research_failed: 1027
- simulated failed buy: 445
- proven_low_volume: 401
- proven_price_collapsed_or_parabolic: 60
- proven: 53
- proven_no_uptrend: 24
- research_passed: 14
- dip: 10

Warning: 280 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
