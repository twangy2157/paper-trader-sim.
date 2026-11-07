# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T04:10:56Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 20. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 924 | 13% | -60.2% | -64 to -56 | -55717 |
| all momentum | 936 | 13% | -59.9% | -64 to -56 | -56112 |
| control | 1167 | 6% | -19.8% | -22 to -18 | -23247 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (915, 14%) | -20% (1167, 6%) | -40% (10, 10%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (915, 15%) | -20% (1167, 7%) | -43% (10, 10%) | -15% (46, 46%) |
| sl30_tp50 | -62% (915, 16%) | -20% (1167, 7%) | -44% (10, 10%) | -17% (46, 46%) |
| sl50_tp50 | -61% (915, 18%) | -21% (1167, 8%) | -47% (10, 10%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (915, 16%) | -21% (1167, 7%) | -40% (10, 10%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 32847. Outcomes:

- missed_window: 21310
- low_liquidity: 5964
- proven_liquidity_gone: 2507
- no_momentum: 1225
- research_failed: 929
- simulated failed buy: 403
- proven_low_volume: 360
- proven_price_collapsed_or_parabolic: 58
- proven: 47
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 255 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
