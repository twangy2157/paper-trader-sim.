# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T17:39:39Z. Bankroll cash (research-selected trades): 913.731903378573. Open positions: 38. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 4 | 25% | -21.2% | - | -86 |
| momentum, not picked | 505 | 15% | -53.5% | -59 to -48 | -27084 |
| all momentum | 509 | 16% | -53.3% | -59 to -48 | -27170 |
| control | 605 | 7% | -18.8% | -22 to -16 | -11452 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 29 | 41% | -18.2% | -37 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (488, 16%) | -19% (605, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| wide_sl50_tp100 | -54% (488, 18%) | -19% (605, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| sl30_tp50 | -56% (488, 19%) | -19% (605, 8%) | -22% (4, 25%) | -20% (29, 41%) |
| sl50_tp50 | -55% (488, 22%) | -19% (605, 9%) | -22% (4, 25%) | -20% (29, 41%) |
| no_stop_tp100 | -53% (488, 19%) | -20% (605, 7%) | -13% (4, 25%) | -18% (29, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18866. Outcomes:

- missed_window: 12477
- low_liquidity: 3503
- proven_liquidity_gone: 1214
- no_momentum: 672
- research_failed: 520
- simulated failed buy: 214
- proven_low_volume: 175
- proven_price_collapsed_or_parabolic: 36
- proven: 29
- proven_no_uptrend: 18
- research_passed: 4
- dip: 4

Warning: 145 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
