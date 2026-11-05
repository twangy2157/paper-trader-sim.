# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T05:23:45Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 21. Pools on watchlist: 35.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 599 | 16% | -54.0% | -59 to -49 | -32412 |
| all momentum | 604 | 16% | -53.9% | -59 to -49 | -32595 |
| control | 729 | 8% | -18.9% | -22 to -16 | -13848 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (583, 16%) | -19% (729, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -54% (583, 18%) | -19% (729, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (583, 20%) | -19% (729, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -55% (583, 22%) | -20% (729, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -53% (583, 19%) | -20% (729, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21579. Outcomes:

- missed_window: 14149
- low_liquidity: 3992
- proven_liquidity_gone: 1477
- no_momentum: 785
- research_failed: 605
- simulated failed buy: 243
- proven_low_volume: 218
- proven_price_collapsed_or_parabolic: 46
- proven: 35
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 163 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
