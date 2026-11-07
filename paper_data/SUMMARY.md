# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T04:41:35Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 26. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 927 | 13% | -60.3% | -64 to -56 | -56017 |
| all momentum | 939 | 13% | -60.0% | -64 to -56 | -56412 |
| control | 1173 | 6% | -19.8% | -22 to -18 | -23391 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (918, 14%) | -20% (1173, 6%) | -40% (10, 10%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (918, 15%) | -20% (1173, 7%) | -43% (10, 10%) | -15% (46, 46%) |
| sl30_tp50 | -62% (918, 16%) | -20% (1173, 7%) | -44% (10, 10%) | -17% (46, 46%) |
| sl50_tp50 | -61% (918, 18%) | -21% (1173, 8%) | -47% (10, 10%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (918, 16%) | -21% (1173, 7%) | -40% (10, 10%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 32989. Outcomes:

- missed_window: 21400
- low_liquidity: 5984
- proven_liquidity_gone: 2519
- no_momentum: 1233
- research_failed: 936
- simulated failed buy: 406
- proven_low_volume: 362
- proven_price_collapsed_or_parabolic: 58
- proven: 47
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 258 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
