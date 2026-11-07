# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T02:58:20Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 27. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 911 | 13% | -60.2% | -64 to -56 | -54891 |
| all momentum | 923 | 14% | -59.8% | -64 to -56 | -55286 |
| control | 1152 | 6% | -19.8% | -22 to -18 | -22877 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (902, 14%) | -20% (1152, 6%) | -43% (9, 11%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (902, 15%) | -20% (1152, 7%) | -47% (9, 11%) | -15% (46, 46%) |
| sl30_tp50 | -62% (902, 16%) | -20% (1152, 7%) | -47% (9, 11%) | -17% (46, 46%) |
| sl50_tp50 | -61% (902, 19%) | -20% (1152, 8%) | -50% (9, 11%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (902, 16%) | -21% (1152, 7%) | -43% (9, 11%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 32479. Outcomes:

- missed_window: 21058
- low_liquidity: 5915
- proven_liquidity_gone: 2474
- no_momentum: 1210
- research_failed: 923
- simulated failed buy: 401
- proven_low_volume: 351
- proven_price_collapsed_or_parabolic: 57
- proven: 46
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 254 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
