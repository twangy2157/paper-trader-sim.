# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T15:33:20Z. Bankroll cash (research-selected trades): 759.5946161788225. Open positions: 25. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 492 | 15% | -54.2% | -60 to -48 | -26733 |
| all momentum | 494 | 15% | -54.3% | -60 to -49 | -26874 |
| control | 589 | 7% | -18.3% | -21 to -15 | -10844 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 26 | 38% | -16.6% | -37 to 3 | -434 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (473, 15%) | -18% (589, 7%) | -13% (4, 25%) | -17% (26, 38%) |
| wide_sl50_tp100 | -55% (473, 17%) | -19% (589, 8%) | -13% (4, 25%) | -17% (26, 38%) |
| sl30_tp50 | -57% (473, 19%) | -19% (589, 8%) | -22% (4, 25%) | -18% (26, 38%) |
| sl50_tp50 | -56% (473, 21%) | -19% (589, 9%) | -22% (4, 25%) | -18% (26, 38%) |
| no_stop_tp100 | -54% (473, 18%) | -19% (589, 8%) | -13% (4, 25%) | -17% (26, 38%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18240. Outcomes:

- missed_window: 12059
- low_liquidity: 3409
- proven_liquidity_gone: 1160
- no_momentum: 645
- research_failed: 501
- simulated failed buy: 208
- proven_low_volume: 174
- proven_price_collapsed_or_parabolic: 33
- proven: 29
- proven_no_uptrend: 15
- dip: 4
- research_passed: 3

Warning: 138 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
