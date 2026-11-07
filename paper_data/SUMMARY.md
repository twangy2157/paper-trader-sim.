# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T03:08:29Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 25. Pools on watchlist: 52.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 912 | 13% | -60.1% | -64 to -56 | -54927 |
| all momentum | 924 | 14% | -59.8% | -64 to -56 | -55321 |
| control | 1155 | 6% | -19.8% | -22 to -18 | -22961 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (903, 14%) | -20% (1155, 6%) | -43% (9, 11%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (903, 15%) | -20% (1155, 7%) | -47% (9, 11%) | -15% (46, 46%) |
| sl30_tp50 | -62% (903, 16%) | -20% (1155, 7%) | -47% (9, 11%) | -17% (46, 46%) |
| sl50_tp50 | -61% (903, 18%) | -20% (1155, 8%) | -50% (9, 11%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (903, 16%) | -21% (1155, 7%) | -43% (9, 11%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 32532. Outcomes:

- missed_window: 21095
- low_liquidity: 5923
- proven_liquidity_gone: 2480
- no_momentum: 1211
- research_failed: 924
- simulated failed buy: 401
- proven_low_volume: 351
- proven_price_collapsed_or_parabolic: 57
- proven: 46
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 254 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
