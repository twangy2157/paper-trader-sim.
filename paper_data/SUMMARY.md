# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T07:26:11Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 6. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 435 | 15% | -54.3% | -60 to -48 | -23664 |
| all momentum | 437 | 15% | -54.4% | -60 to -48 | -23804 |
| control | 516 | 8% | -16.7% | -20 to -14 | -8689 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 20 | 30% | -29.0% | -50 to -9 | -581 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (416, 16%) | -17% (516, 8%) | -13% (4, 25%) | -29% (20, 30%) |
| wide_sl50_tp100 | -55% (416, 17%) | -17% (516, 8%) | -13% (4, 25%) | -29% (20, 30%) |
| sl30_tp50 | -57% (416, 19%) | -17% (516, 9%) | -22% (4, 25%) | -29% (20, 30%) |
| sl50_tp50 | -56% (416, 21%) | -17% (516, 9%) | -22% (4, 25%) | -29% (20, 30%) |
| no_stop_tp100 | -55% (416, 18%) | -18% (516, 8%) | -13% (4, 25%) | -29% (20, 30%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16232. Outcomes:

- missed_window: 10795
- low_liquidity: 3077
- proven_liquidity_gone: 969
- no_momentum: 563
- research_failed: 437
- simulated failed buy: 177
- proven_low_volume: 151
- proven_price_collapsed_or_parabolic: 25
- proven: 21
- proven_no_uptrend: 11
- dip: 4
- research_passed: 2

Warning: 122 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
