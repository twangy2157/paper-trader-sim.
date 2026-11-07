# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T08:29:54Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 32. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 953 | 13% | -60.4% | -64 to -57 | -57676 |
| all momentum | 965 | 13% | -60.1% | -64 to -56 | -58071 |
| control | 1212 | 6% | -19.9% | -22 to -18 | -24268 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 47 | 47% | -14.4% | -29 to -1 | -682 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (944, 13%) | -20% (1212, 6%) | -40% (10, 10%) | -14% (47, 47%) |
| wide_sl50_tp100 | -60% (944, 15%) | -20% (1212, 7%) | -43% (10, 10%) | -14% (47, 47%) |
| sl30_tp50 | -62% (944, 16%) | -20% (1212, 7%) | -44% (10, 10%) | -17% (47, 47%) |
| sl50_tp50 | -61% (944, 18%) | -21% (1212, 8%) | -47% (10, 10%) | -17% (47, 47%) |
| no_stop_tp100 | -60% (944, 16%) | -21% (1212, 7%) | -40% (10, 10%) | -14% (47, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 33929. Outcomes:

- missed_window: 21996
- low_liquidity: 6134
- proven_liquidity_gone: 2613
- no_momentum: 1276
- research_failed: 961
- simulated failed buy: 417
- proven_low_volume: 378
- proven_price_collapsed_or_parabolic: 58
- proven: 51
- proven_no_uptrend: 23
- research_passed: 12
- dip: 10

Warning: 266 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
