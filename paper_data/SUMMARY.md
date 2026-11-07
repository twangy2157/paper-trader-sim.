# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T07:45:11Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 27. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 946 | 13% | -60.3% | -64 to -56 | -57136 |
| all momentum | 958 | 13% | -60.0% | -64 to -56 | -57531 |
| control | 1205 | 6% | -20.0% | -22 to -18 | -24158 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 47 | 47% | -14.4% | -29 to -1 | -682 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (937, 14%) | -20% (1205, 6%) | -40% (10, 10%) | -14% (47, 47%) |
| wide_sl50_tp100 | -60% (937, 15%) | -20% (1205, 7%) | -43% (10, 10%) | -14% (47, 47%) |
| sl30_tp50 | -62% (937, 16%) | -20% (1205, 7%) | -44% (10, 10%) | -17% (47, 47%) |
| sl50_tp50 | -61% (937, 18%) | -21% (1205, 8%) | -47% (10, 10%) | -17% (47, 47%) |
| no_stop_tp100 | -60% (937, 16%) | -21% (1205, 7%) | -40% (10, 10%) | -14% (47, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 33722. Outcomes:

- missed_window: 21865
- low_liquidity: 6104
- proven_liquidity_gone: 2592
- no_momentum: 1261
- research_failed: 958
- simulated failed buy: 416
- proven_low_volume: 373
- proven_price_collapsed_or_parabolic: 58
- proven: 50
- proven_no_uptrend: 23
- research_passed: 12
- dip: 10

Warning: 266 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
