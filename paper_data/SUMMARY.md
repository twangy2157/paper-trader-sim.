# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T01:14:11Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 10. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 905 | 13% | -60.1% | -64 to -56 | -54484 |
| all momentum | 917 | 14% | -59.8% | -64 to -56 | -54879 |
| control | 1132 | 6% | -19.9% | -22 to -18 | -22635 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (896, 14%) | -20% (1132, 6%) | -43% (9, 11%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (896, 15%) | -20% (1132, 7%) | -47% (9, 11%) | -15% (46, 46%) |
| sl30_tp50 | -62% (896, 16%) | -20% (1132, 7%) | -47% (9, 11%) | -17% (46, 46%) |
| sl50_tp50 | -61% (896, 19%) | -21% (1132, 8%) | -50% (9, 11%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (896, 16%) | -21% (1132, 7%) | -43% (9, 11%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 31981. Outcomes:

- missed_window: 20737
- low_liquidity: 5835
- proven_liquidity_gone: 2441
- no_momentum: 1184
- research_failed: 907
- simulated failed buy: 396
- proven_low_volume: 335
- proven_price_collapsed_or_parabolic: 57
- proven: 46
- proven_no_uptrend: 22
- research_passed: 12
- dip: 9

Warning: 250 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
