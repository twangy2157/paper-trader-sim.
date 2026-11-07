# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T03:40:10Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 18. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 920 | 13% | -60.2% | -64 to -56 | -55509 |
| all momentum | 932 | 13% | -59.9% | -63 to -56 | -55904 |
| control | 1162 | 6% | -19.8% | -22 to -18 | -23122 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (911, 14%) | -20% (1162, 6%) | -40% (10, 10%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (911, 15%) | -20% (1162, 7%) | -43% (10, 10%) | -15% (46, 46%) |
| sl30_tp50 | -62% (911, 16%) | -20% (1162, 7%) | -44% (10, 10%) | -17% (46, 46%) |
| sl50_tp50 | -61% (911, 18%) | -21% (1162, 8%) | -47% (10, 10%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (911, 16%) | -21% (1162, 7%) | -40% (10, 10%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 32684. Outcomes:

- missed_window: 21204
- low_liquidity: 5938
- proven_liquidity_gone: 2493
- no_momentum: 1217
- research_failed: 927
- simulated failed buy: 402
- proven_low_volume: 355
- proven_price_collapsed_or_parabolic: 58
- proven: 46
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 255 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
