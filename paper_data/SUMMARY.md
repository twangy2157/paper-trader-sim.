# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T05:03:00Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 28. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 928 | 13% | -60.3% | -64 to -57 | -56059 |
| all momentum | 940 | 13% | -60.0% | -64 to -56 | -56454 |
| control | 1178 | 6% | -20.0% | -22 to -18 | -23697 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (919, 14%) | -20% (1178, 6%) | -40% (10, 10%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (919, 15%) | -20% (1178, 7%) | -43% (10, 10%) | -15% (46, 46%) |
| sl30_tp50 | -62% (919, 16%) | -20% (1178, 7%) | -44% (10, 10%) | -17% (46, 46%) |
| sl50_tp50 | -61% (919, 18%) | -21% (1178, 8%) | -47% (10, 10%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (919, 16%) | -21% (1178, 7%) | -40% (10, 10%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 33076. Outcomes:

- missed_window: 21452
- low_liquidity: 6004
- proven_liquidity_gone: 2521
- no_momentum: 1237
- research_failed: 940
- simulated failed buy: 409
- proven_low_volume: 364
- proven_price_collapsed_or_parabolic: 58
- proven: 47
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 261 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
