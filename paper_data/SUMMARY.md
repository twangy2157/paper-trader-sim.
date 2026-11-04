# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T05:49:08Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 16. Pools on watchlist: 81.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 424 | 15% | -53.7% | -60 to -48 | -22792 |
| all momentum | 426 | 15% | -53.7% | -59 to -48 | -22932 |
| control | 500 | 8% | -16.3% | -19 to -13 | -8184 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (405, 16%) | -16% (500, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (405, 17%) | -17% (500, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -56% (405, 19%) | -17% (500, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (405, 21%) | -17% (500, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -54% (405, 18%) | -17% (500, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15879. Outcomes:

- missed_window: 10537
- low_liquidity: 3038
- proven_liquidity_gone: 938
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
