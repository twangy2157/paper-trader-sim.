# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T19:14:45Z. Bankroll cash (research-selected trades): 813.731903378573. Open positions: 9. Pools on watchlist: 73.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 4 | 25% | -21.2% | - | -86 |
| momentum, not picked | 521 | 16% | -53.0% | -59 to -47 | -27664 |
| all momentum | 525 | 16% | -52.8% | -58 to -47 | -27750 |
| control | 631 | 7% | -19.0% | -22 to -16 | -12065 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 29 | 41% | -18.2% | -37 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (504, 16%) | -19% (631, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| wide_sl50_tp100 | -53% (504, 18%) | -19% (631, 8%) | -13% (4, 25%) | -18% (29, 41%) |
| sl30_tp50 | -55% (504, 20%) | -19% (631, 8%) | -22% (4, 25%) | -20% (29, 41%) |
| sl50_tp50 | -54% (504, 23%) | -19% (631, 9%) | -22% (4, 25%) | -20% (29, 41%) |
| no_stop_tp100 | -52% (504, 19%) | -20% (631, 8%) | -13% (4, 25%) | -18% (29, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 19174. Outcomes:

- missed_window: 12691
- low_liquidity: 3538
- proven_liquidity_gone: 1249
- no_momentum: 679
- research_failed: 524
- simulated failed buy: 219
- proven_low_volume: 178
- proven_price_collapsed_or_parabolic: 38
- proven: 30
- proven_no_uptrend: 19
- research_passed: 5
- dip: 4

Warning: 147 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
