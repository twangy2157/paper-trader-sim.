# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T14:51:55Z. Bankroll cash (research-selected trades): 859.5946161788225. Open positions: 28. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 485 | 15% | -54.1% | -60 to -48 | -26279 |
| all momentum | 487 | 15% | -54.2% | -60 to -48 | -26419 |
| control | 582 | 7% | -18.1% | -21 to -15 | -10582 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 25 | 36% | -21.0% | -39 to -4 | -528 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (466, 16%) | -18% (582, 7%) | -13% (4, 25%) | -21% (25, 36%) |
| wide_sl50_tp100 | -55% (466, 17%) | -18% (582, 8%) | -13% (4, 25%) | -21% (25, 36%) |
| sl30_tp50 | -57% (466, 19%) | -19% (582, 8%) | -22% (4, 25%) | -21% (25, 36%) |
| sl50_tp50 | -56% (466, 21%) | -19% (582, 9%) | -22% (4, 25%) | -21% (25, 36%) |
| no_stop_tp100 | -54% (466, 18%) | -19% (582, 8%) | -13% (4, 25%) | -21% (25, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18081. Outcomes:

- missed_window: 11962
- low_liquidity: 3382
- proven_liquidity_gone: 1143
- no_momentum: 639
- research_failed: 496
- simulated failed buy: 203
- proven_low_volume: 173
- proven_price_collapsed_or_parabolic: 33
- proven: 29
- proven_no_uptrend: 15
- dip: 4
- research_passed: 2

Warning: 135 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
