# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T05:37:40Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 22. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 423 | 15% | -54.0% | -60 to -48 | -22885 |
| all momentum | 425 | 15% | -54.1% | -60 to -48 | -23025 |
| control | 495 | 8% | -16.6% | -20 to -13 | -8246 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (404, 16%) | -17% (495, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (404, 17%) | -17% (495, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (404, 19%) | -17% (495, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (404, 21%) | -17% (495, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (404, 18%) | -17% (495, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15828. Outcomes:

- missed_window: 10502
- low_liquidity: 3030
- proven_liquidity_gone: 930
- no_momentum: 553
- research_failed: 429
- simulated failed buy: 175
- proven_low_volume: 150
- proven_price_collapsed_or_parabolic: 22
- proven: 21
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 121 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
