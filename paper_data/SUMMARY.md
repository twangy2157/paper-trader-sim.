# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T09:12:11Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 32. Pools on watchlist: 37.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 961 | 13% | -60.5% | -64 to -57 | -58263 |
| all momentum | 973 | 13% | -60.2% | -64 to -56 | -58658 |
| control | 1220 | 6% | -19.9% | -22 to -18 | -24401 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 47 | 47% | -14.4% | -29 to -1 | -682 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (952, 13%) | -20% (1220, 6%) | -40% (10, 10%) | -14% (47, 47%) |
| wide_sl50_tp100 | -60% (952, 15%) | -20% (1220, 7%) | -43% (10, 10%) | -14% (47, 47%) |
| sl30_tp50 | -62% (952, 16%) | -20% (1220, 7%) | -44% (10, 10%) | -17% (47, 47%) |
| sl50_tp50 | -61% (952, 18%) | -21% (1220, 8%) | -47% (10, 10%) | -17% (47, 47%) |
| no_stop_tp100 | -60% (952, 16%) | -21% (1220, 7%) | -40% (10, 10%) | -14% (47, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 34088. Outcomes:

- missed_window: 22090
- low_liquidity: 6169
- proven_liquidity_gone: 2626
- no_momentum: 1287
- research_failed: 966
- simulated failed buy: 418
- proven_low_volume: 378
- proven_price_collapsed_or_parabolic: 58
- proven: 51
- proven_no_uptrend: 23
- research_passed: 12
- dip: 10

Warning: 266 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
