# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T13:27:38Z. Bankroll cash (research-selected trades): 859.5946161788225. Open positions: 16. Pools on watchlist: 92.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 480 | 15% | -53.9% | -59 to -48 | -25903 |
| all momentum | 482 | 15% | -53.9% | -60 to -48 | -26043 |
| control | 570 | 7% | -17.6% | -21 to -15 | -10101 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 24 | 33% | -22.9% | -41 to -6 | -549 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (461, 16%) | -18% (570, 7%) | -13% (4, 25%) | -23% (24, 33%) |
| wide_sl50_tp100 | -55% (461, 17%) | -18% (570, 8%) | -13% (4, 25%) | -23% (24, 33%) |
| sl30_tp50 | -56% (461, 19%) | -18% (570, 8%) | -22% (4, 25%) | -23% (24, 33%) |
| sl50_tp50 | -56% (461, 21%) | -18% (570, 9%) | -22% (4, 25%) | -23% (24, 33%) |
| no_stop_tp100 | -54% (461, 18%) | -18% (570, 8%) | -13% (4, 25%) | -23% (24, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 17643. Outcomes:

- missed_window: 11669
- low_liquidity: 3309
- proven_liquidity_gone: 1115
- no_momentum: 624
- research_failed: 483
- simulated failed buy: 196
- proven_low_volume: 167
- proven_price_collapsed_or_parabolic: 32
- proven: 27
- proven_no_uptrend: 15
- dip: 4
- research_passed: 2

Warning: 132 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
