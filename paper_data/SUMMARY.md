# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T03:19:45Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 20. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 916 | 13% | -60.2% | -64 to -56 | -55205 |
| all momentum | 928 | 13% | -59.8% | -63 to -56 | -55600 |
| control | 1157 | 6% | -19.8% | -22 to -18 | -23065 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (907, 14%) | -20% (1157, 6%) | -40% (10, 10%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (907, 15%) | -20% (1157, 7%) | -43% (10, 10%) | -15% (46, 46%) |
| sl30_tp50 | -62% (907, 16%) | -20% (1157, 7%) | -44% (10, 10%) | -17% (46, 46%) |
| sl50_tp50 | -61% (907, 18%) | -21% (1157, 8%) | -47% (10, 10%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (907, 16%) | -21% (1157, 7%) | -40% (10, 10%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 32581. Outcomes:

- missed_window: 21133
- low_liquidity: 5926
- proven_liquidity_gone: 2485
- no_momentum: 1212
- research_failed: 925
- simulated failed buy: 401
- proven_low_volume: 352
- proven_price_collapsed_or_parabolic: 57
- proven: 46
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 254 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
