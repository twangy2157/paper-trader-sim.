# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T04:43:38Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 18. Pools on watchlist: 92.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 416 | 15% | -54.2% | -60 to -48 | -22568 |
| all momentum | 418 | 15% | -54.2% | -60 to -48 | -22708 |
| control | 489 | 8% | -16.3% | -19 to -13 | -8004 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (397, 16%) | -16% (489, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (397, 17%) | -17% (489, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (397, 19%) | -17% (489, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (397, 21%) | -17% (489, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (397, 18%) | -17% (489, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15509. Outcomes:

- missed_window: 10278
- low_liquidity: 2983
- proven_liquidity_gone: 905
- no_momentum: 542
- research_failed: 424
- simulated failed buy: 171
- proven_low_volume: 148
- proven_price_collapsed_or_parabolic: 22
- proven: 20
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 118 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
