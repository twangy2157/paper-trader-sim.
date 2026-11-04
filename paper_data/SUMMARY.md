# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T14:11:12Z. Bankroll cash (research-selected trades): 859.5946161788225. Open positions: 21. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 482 | 15% | -53.8% | -60 to -48 | -25977 |
| all momentum | 484 | 15% | -53.9% | -60 to -48 | -26118 |
| control | 575 | 7% | -17.6% | -21 to -15 | -10182 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 25 | 36% | -21.0% | -39 to -4 | -528 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (463, 16%) | -18% (575, 7%) | -13% (4, 25%) | -21% (25, 36%) |
| wide_sl50_tp100 | -55% (463, 17%) | -18% (575, 8%) | -13% (4, 25%) | -21% (25, 36%) |
| sl30_tp50 | -56% (463, 19%) | -18% (575, 8%) | -22% (4, 25%) | -21% (25, 36%) |
| sl50_tp50 | -56% (463, 21%) | -18% (575, 9%) | -22% (4, 25%) | -21% (25, 36%) |
| no_stop_tp100 | -54% (463, 19%) | -18% (575, 8%) | -13% (4, 25%) | -21% (25, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 17885. Outcomes:

- missed_window: 11834
- low_liquidity: 3349
- proven_liquidity_gone: 1134
- no_momentum: 630
- research_failed: 490
- simulated failed buy: 199
- proven_low_volume: 168
- proven_price_collapsed_or_parabolic: 33
- proven: 27
- proven_no_uptrend: 15
- dip: 4
- research_passed: 2

Warning: 134 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
