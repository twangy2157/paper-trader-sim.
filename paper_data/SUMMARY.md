# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T05:24:39Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 22. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 932 | 13% | -60.2% | -64 to -56 | -56200 |
| all momentum | 944 | 13% | -59.9% | -64 to -56 | -56595 |
| control | 1184 | 6% | -20.0% | -22 to -18 | -23827 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (923, 14%) | -20% (1184, 6%) | -40% (10, 10%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (923, 15%) | -21% (1184, 7%) | -43% (10, 10%) | -15% (46, 46%) |
| sl30_tp50 | -62% (923, 16%) | -20% (1184, 7%) | -44% (10, 10%) | -17% (46, 46%) |
| sl50_tp50 | -61% (923, 18%) | -21% (1184, 8%) | -47% (10, 10%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (923, 16%) | -21% (1184, 7%) | -40% (10, 10%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 33175. Outcomes:

- missed_window: 21519
- low_liquidity: 6020
- proven_liquidity_gone: 2530
- no_momentum: 1239
- research_failed: 942
- simulated failed buy: 409
- proven_low_volume: 367
- proven_price_collapsed_or_parabolic: 58
- proven: 47
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 261 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
