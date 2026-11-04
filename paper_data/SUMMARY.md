# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T12:42:55Z. Bankroll cash (research-selected trades): 859.5946161788225. Open positions: 16. Pools on watchlist: 9.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 478 | 15% | -54.1% | -60 to -48 | -25880 |
| all momentum | 480 | 15% | -54.1% | -60 to -48 | -26020 |
| control | 568 | 7% | -17.5% | -20 to -15 | -9991 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 22 | 36% | -24.6% | -45 to -5 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (459, 16%) | -17% (568, 7%) | -13% (4, 25%) | -25% (22, 36%) |
| wide_sl50_tp100 | -55% (459, 17%) | -18% (568, 8%) | -13% (4, 25%) | -25% (22, 36%) |
| sl30_tp50 | -57% (459, 19%) | -18% (568, 8%) | -22% (4, 25%) | -25% (22, 36%) |
| sl50_tp50 | -56% (459, 21%) | -18% (568, 9%) | -22% (4, 25%) | -25% (22, 36%) |
| no_stop_tp100 | -54% (459, 19%) | -18% (568, 8%) | -13% (4, 25%) | -25% (22, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 17477. Outcomes:

- missed_window: 11551
- low_liquidity: 3285
- proven_liquidity_gone: 1099
- no_momentum: 619
- research_failed: 482
- simulated failed buy: 195
- proven_low_volume: 167
- proven_price_collapsed_or_parabolic: 31
- proven: 27
- proven_no_uptrend: 15
- dip: 4
- research_passed: 2

Warning: 132 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
