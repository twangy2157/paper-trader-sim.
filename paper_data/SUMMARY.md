# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T10:47:09Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 22. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 968 | 13% | -60.7% | -64 to -57 | -58840 |
| all momentum | 980 | 13% | -60.3% | -64 to -57 | -59235 |
| control | 1245 | 6% | -20.1% | -22 to -18 | -25106 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 50 | 46% | -17.2% | -31 to -4 | -865 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (959, 13%) | -20% (1245, 6%) | -40% (10, 10%) | -17% (50, 46%) |
| wide_sl50_tp100 | -61% (959, 15%) | -21% (1245, 7%) | -43% (10, 10%) | -17% (50, 46%) |
| sl30_tp50 | -62% (959, 16%) | -20% (1245, 7%) | -44% (10, 10%) | -19% (50, 46%) |
| sl50_tp50 | -62% (959, 18%) | -21% (1245, 7%) | -47% (10, 10%) | -19% (50, 46%) |
| no_stop_tp100 | -60% (959, 16%) | -21% (1245, 7%) | -40% (10, 10%) | -17% (50, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 34471. Outcomes:

- missed_window: 22328
- low_liquidity: 6233
- proven_liquidity_gone: 2669
- no_momentum: 1300
- research_failed: 977
- simulated failed buy: 426
- proven_low_volume: 383
- proven_price_collapsed_or_parabolic: 58
- proven: 52
- proven_no_uptrend: 23
- research_passed: 12
- dip: 10

Warning: 268 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
