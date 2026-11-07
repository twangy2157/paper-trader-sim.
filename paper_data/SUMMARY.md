# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T10:26:45Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 15. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 967 | 13% | -60.6% | -64 to -56 | -58739 |
| all momentum | 979 | 13% | -60.3% | -64 to -57 | -59134 |
| control | 1244 | 6% | -20.1% | -22 to -18 | -25102 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 48 | 46% | -16.2% | -30 to -3 | -783 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (958, 13%) | -20% (1244, 6%) | -40% (10, 10%) | -16% (48, 46%) |
| wide_sl50_tp100 | -61% (958, 15%) | -21% (1244, 7%) | -43% (10, 10%) | -16% (48, 46%) |
| sl30_tp50 | -62% (958, 16%) | -20% (1244, 7%) | -44% (10, 10%) | -18% (48, 46%) |
| sl50_tp50 | -62% (958, 18%) | -21% (1244, 7%) | -47% (10, 10%) | -18% (48, 46%) |
| no_stop_tp100 | -60% (958, 16%) | -21% (1244, 7%) | -40% (10, 10%) | -16% (48, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 34387. Outcomes:

- missed_window: 22280
- low_liquidity: 6219
- proven_liquidity_gone: 2663
- no_momentum: 1295
- research_failed: 971
- simulated failed buy: 423
- proven_low_volume: 381
- proven_price_collapsed_or_parabolic: 58
- proven: 52
- proven_no_uptrend: 23
- research_passed: 12
- dip: 10

Warning: 268 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
