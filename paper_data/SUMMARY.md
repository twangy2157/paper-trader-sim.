# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T00:25:34Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 14. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 383 | 14% | -54.7% | -61 to -48 | -20968 |
| all momentum | 385 | 14% | -54.7% | -61 to -48 | -21108 |
| control | 462 | 8% | -16.0% | -19 to -13 | -7456 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 18 | 33% | -31.9% | -56 to -9 | -575 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (364, 15%) | -16% (462, 8%) | -13% (4, 25%) | -32% (18, 33%) |
| wide_sl50_tp100 | -56% (364, 16%) | -16% (462, 8%) | -13% (4, 25%) | -32% (18, 33%) |
| sl30_tp50 | -57% (364, 19%) | -17% (462, 8%) | -22% (4, 25%) | -32% (18, 33%) |
| sl50_tp50 | -57% (364, 21%) | -17% (462, 8%) | -22% (4, 25%) | -32% (18, 33%) |
| no_stop_tp100 | -56% (364, 17%) | -17% (462, 8%) | -13% (4, 25%) | -32% (18, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 14349. Outcomes:

- missed_window: 9512
- low_liquidity: 2786
- proven_liquidity_gone: 795
- no_momentum: 509
- research_failed: 393
- simulated failed buy: 157
- proven_low_volume: 142
- proven_price_collapsed_or_parabolic: 20
- proven: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 107 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
