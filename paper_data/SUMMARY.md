# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T14:31:41Z. Bankroll cash (research-selected trades): 859.5946161788225. Open positions: 21. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 483 | 15% | -53.9% | -59 to -48 | -26077 |
| all momentum | 485 | 15% | -54.0% | -60 to -48 | -26218 |
| control | 580 | 7% | -17.9% | -21 to -15 | -10419 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 25 | 36% | -21.0% | -39 to -4 | -528 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (464, 16%) | -18% (580, 7%) | -13% (4, 25%) | -21% (25, 36%) |
| wide_sl50_tp100 | -55% (464, 17%) | -18% (580, 8%) | -13% (4, 25%) | -21% (25, 36%) |
| sl30_tp50 | -56% (464, 19%) | -18% (580, 8%) | -22% (4, 25%) | -21% (25, 36%) |
| sl50_tp50 | -56% (464, 21%) | -18% (580, 9%) | -22% (4, 25%) | -21% (25, 36%) |
| no_stop_tp100 | -54% (464, 19%) | -19% (580, 8%) | -13% (4, 25%) | -21% (25, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 17990. Outcomes:

- missed_window: 11904
- low_liquidity: 3365
- proven_liquidity_gone: 1141
- no_momentum: 633
- research_failed: 492
- simulated failed buy: 200
- proven_low_volume: 173
- proven_price_collapsed_or_parabolic: 33
- proven: 28
- proven_no_uptrend: 15
- dip: 4
- research_passed: 2

Warning: 135 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
