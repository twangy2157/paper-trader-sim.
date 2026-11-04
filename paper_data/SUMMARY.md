# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T15:12:50Z. Bankroll cash (research-selected trades): 759.5946161788225. Open positions: 31. Pools on watchlist: 30.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 489 | 15% | -54.2% | -60 to -48 | -26525 |
| all momentum | 491 | 15% | -54.2% | -60 to -48 | -26666 |
| control | 585 | 7% | -18.3% | -21 to -15 | -10787 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 25 | 36% | -21.0% | -39 to -4 | -528 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (470, 16%) | -18% (585, 7%) | -13% (4, 25%) | -21% (25, 36%) |
| wide_sl50_tp100 | -55% (470, 17%) | -19% (585, 8%) | -13% (4, 25%) | -21% (25, 36%) |
| sl30_tp50 | -57% (470, 19%) | -19% (585, 8%) | -22% (4, 25%) | -21% (25, 36%) |
| sl50_tp50 | -56% (470, 21%) | -19% (585, 9%) | -22% (4, 25%) | -21% (25, 36%) |
| no_stop_tp100 | -54% (470, 19%) | -19% (585, 8%) | -13% (4, 25%) | -21% (25, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18154. Outcomes:

- missed_window: 12005
- low_liquidity: 3392
- proven_liquidity_gone: 1148
- no_momentum: 645
- research_failed: 499
- simulated failed buy: 208
- proven_low_volume: 173
- proven_price_collapsed_or_parabolic: 33
- proven: 29
- proven_no_uptrend: 15
- dip: 4
- research_passed: 3

Warning: 138 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
