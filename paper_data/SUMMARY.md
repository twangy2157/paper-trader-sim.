# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T05:57:30Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 21. Pools on watchlist: 35.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 601 | 16% | -54.2% | -59 to -49 | -32612 |
| all momentum | 606 | 16% | -54.0% | -59 to -49 | -32795 |
| control | 737 | 8% | -18.8% | -21 to -16 | -13895 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (585, 16%) | -19% (737, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -54% (585, 18%) | -19% (737, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (585, 19%) | -19% (737, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -55% (585, 22%) | -19% (737, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -54% (585, 19%) | -19% (737, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21693. Outcomes:

- missed_window: 14212
- low_liquidity: 4014
- proven_liquidity_gone: 1493
- no_momentum: 789
- research_failed: 611
- simulated failed buy: 243
- proven_low_volume: 219
- proven_price_collapsed_or_parabolic: 48
- proven: 35
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 163 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
