# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T16:57:21Z. Bankroll cash (research-selected trades): 752.0843857041315. Open positions: 23. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 3 | 0% | -48.8% | - | -148 |
| momentum, not picked | 502 | 15% | -53.7% | -59 to -48 | -27012 |
| all momentum | 505 | 15% | -53.7% | -59 to -48 | -27159 |
| control | 603 | 7% | -18.7% | -22 to -16 | -11343 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 27 | 41% | -15.9% | -35 to 2 | -431 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (484, 16%) | -19% (603, 7%) | -13% (4, 25%) | -16% (27, 41%) |
| wide_sl50_tp100 | -54% (484, 18%) | -19% (603, 7%) | -13% (4, 25%) | -16% (27, 41%) |
| sl30_tp50 | -56% (484, 19%) | -19% (603, 8%) | -22% (4, 25%) | -18% (27, 41%) |
| sl50_tp50 | -56% (484, 21%) | -19% (603, 9%) | -22% (4, 25%) | -18% (27, 41%) |
| no_stop_tp100 | -53% (484, 19%) | -20% (603, 7%) | -13% (4, 25%) | -16% (27, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18678. Outcomes:

- missed_window: 12360
- low_liquidity: 3475
- proven_liquidity_gone: 1198
- no_momentum: 659
- research_failed: 510
- simulated failed buy: 214
- proven_low_volume: 175
- proven_price_collapsed_or_parabolic: 35
- proven: 29
- proven_no_uptrend: 15
- research_passed: 4
- dip: 4

Warning: 144 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
