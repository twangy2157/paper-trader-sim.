# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T00:13:42Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 18. Pools on watchlist: 17.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 383 | 14% | -54.7% | -61 to -48 | -20968 |
| all momentum | 385 | 14% | -54.7% | -61 to -48 | -21108 |
| control | 455 | 7% | -16.3% | -20 to -13 | -7449 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 18 | 33% | -31.9% | -56 to -9 | -575 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (364, 15%) | -16% (455, 7%) | -13% (4, 25%) | -32% (18, 33%) |
| wide_sl50_tp100 | -56% (364, 16%) | -17% (455, 8%) | -13% (4, 25%) | -32% (18, 33%) |
| sl30_tp50 | -57% (364, 19%) | -17% (455, 8%) | -22% (4, 25%) | -32% (18, 33%) |
| sl50_tp50 | -57% (364, 21%) | -17% (455, 8%) | -22% (4, 25%) | -32% (18, 33%) |
| no_stop_tp100 | -56% (364, 17%) | -17% (455, 8%) | -13% (4, 25%) | -32% (18, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 14323. Outcomes:

- missed_window: 9501
- low_liquidity: 2780
- proven_liquidity_gone: 790
- no_momentum: 509
- research_failed: 390
- simulated failed buy: 156
- proven_low_volume: 142
- proven_price_collapsed_or_parabolic: 20
- proven: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 105 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
