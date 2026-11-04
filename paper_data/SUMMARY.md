# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T04:32:09Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 17. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 414 | 15% | -54.0% | -60 to -48 | -22398 |
| all momentum | 416 | 15% | -54.1% | -60 to -48 | -22538 |
| control | 487 | 8% | -16.3% | -20 to -13 | -7985 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (395, 16%) | -16% (487, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (395, 17%) | -17% (487, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (395, 19%) | -17% (487, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (395, 21%) | -17% (487, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (395, 18%) | -17% (487, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15475. Outcomes:

- missed_window: 10261
- low_liquidity: 2972
- proven_liquidity_gone: 905
- no_momentum: 538
- research_failed: 423
- simulated failed buy: 170
- proven_low_volume: 148
- proven_price_collapsed_or_parabolic: 22
- proven: 20
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 117 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
