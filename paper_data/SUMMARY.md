# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T13:14:40Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 14. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 989 | 13% | -61.1% | -65 to -57 | -60481 |
| all momentum | 1001 | 13% | -60.7% | -64 to -57 | -60876 |
| control | 1268 | 6% | -20.1% | -22 to -18 | -25571 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 51 | 47% | -16.7% | -30 to -3 | -857 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (980, 13%) | -20% (1268, 6%) | -40% (10, 10%) | -17% (51, 47%) |
| wide_sl50_tp100 | -61% (980, 15%) | -21% (1268, 7%) | -43% (10, 10%) | -17% (51, 47%) |
| sl30_tp50 | -62% (980, 16%) | -20% (1268, 7%) | -44% (10, 10%) | -19% (51, 47%) |
| sl50_tp50 | -62% (980, 18%) | -21% (1268, 7%) | -47% (10, 10%) | -19% (51, 47%) |
| no_stop_tp100 | -61% (980, 16%) | -21% (1268, 7%) | -40% (10, 10%) | -17% (51, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 35000. Outcomes:

- missed_window: 22641
- low_liquidity: 6335
- proven_liquidity_gone: 2730
- no_momentum: 1317
- research_failed: 997
- simulated failed buy: 435
- proven_low_volume: 389
- proven_price_collapsed_or_parabolic: 58
- proven: 52
- proven_no_uptrend: 24
- research_passed: 12
- dip: 10

Warning: 273 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
