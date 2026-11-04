# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T01:59:30Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 18. Pools on watchlist: 67.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 393 | 15% | -54.6% | -60 to -48 | -21491 |
| all momentum | 395 | 14% | -54.7% | -61 to -48 | -21631 |
| control | 465 | 8% | -16.2% | -19 to -13 | -7573 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (374, 15%) | -16% (465, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -56% (374, 17%) | -17% (465, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (374, 19%) | -17% (465, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -57% (374, 21%) | -17% (465, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (374, 17%) | -17% (465, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 14692. Outcomes:

- missed_window: 9733
- low_liquidity: 2840
- proven_liquidity_gone: 838
- no_momentum: 518
- research_failed: 402
- simulated failed buy: 162
- proven_low_volume: 143
- proven_price_collapsed_or_parabolic: 21
- proven: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 111 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
