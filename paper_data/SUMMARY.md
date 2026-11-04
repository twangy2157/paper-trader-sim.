# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T06:20:56Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 20. Pools on watchlist: 78.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 426 | 15% | -53.9% | -60 to -48 | -22993 |
| all momentum | 428 | 15% | -54.0% | -60 to -48 | -23133 |
| control | 507 | 8% | -16.6% | -20 to -14 | -8468 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (407, 16%) | -17% (507, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (407, 17%) | -17% (507, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (407, 19%) | -17% (507, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (407, 21%) | -17% (507, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (407, 18%) | -17% (507, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16057. Outcomes:

- missed_window: 10661
- low_liquidity: 3057
- proven_liquidity_gone: 957
- no_momentum: 560
- research_failed: 435
- simulated failed buy: 176
- proven_low_volume: 150
- proven_price_collapsed_or_parabolic: 24
- proven: 21
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 122 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
