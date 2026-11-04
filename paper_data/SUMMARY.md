# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T02:43:43Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 16. Pools on watchlist: 76.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 398 | 15% | -54.8% | -61 to -48 | -21846 |
| all momentum | 400 | 14% | -54.9% | -61 to -49 | -21986 |
| control | 472 | 7% | -16.3% | -19 to -13 | -7723 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (379, 15%) | -16% (472, 7%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -56% (379, 17%) | -17% (472, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (379, 19%) | -17% (472, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -57% (379, 21%) | -17% (472, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -56% (379, 17%) | -17% (472, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 14915. Outcomes:

- missed_window: 9882
- low_liquidity: 2886
- proven_liquidity_gone: 849
- no_momentum: 525
- research_failed: 405
- simulated failed buy: 166
- proven_low_volume: 146
- proven_price_collapsed_or_parabolic: 21
- proven: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 115 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
