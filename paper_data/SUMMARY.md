# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T09:54:21Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 19. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 964 | 13% | -60.5% | -64 to -57 | -58439 |
| all momentum | 976 | 13% | -60.2% | -64 to -57 | -58833 |
| control | 1236 | 6% | -19.9% | -22 to -18 | -24767 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 48 | 46% | -16.2% | -30 to -3 | -783 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (955, 13%) | -20% (1236, 6%) | -40% (10, 10%) | -16% (48, 46%) |
| wide_sl50_tp100 | -60% (955, 15%) | -20% (1236, 7%) | -43% (10, 10%) | -16% (48, 46%) |
| sl30_tp50 | -62% (955, 16%) | -20% (1236, 7%) | -44% (10, 10%) | -18% (48, 46%) |
| sl50_tp50 | -61% (955, 18%) | -21% (1236, 8%) | -47% (10, 10%) | -18% (48, 46%) |
| no_stop_tp100 | -60% (955, 16%) | -21% (1236, 7%) | -40% (10, 10%) | -16% (48, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 34263. Outcomes:

- missed_window: 22203
- low_liquidity: 6199
- proven_liquidity_gone: 2646
- no_momentum: 1291
- research_failed: 969
- simulated failed buy: 421
- proven_low_volume: 380
- proven_price_collapsed_or_parabolic: 58
- proven: 51
- proven_no_uptrend: 23
- research_passed: 12
- dip: 10

Warning: 268 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
