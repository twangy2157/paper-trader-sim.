# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T09:07:44Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 18. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 447 | 15% | -54.7% | -60 to -48 | -24467 |
| all momentum | 449 | 15% | -54.7% | -60 to -49 | -24607 |
| control | 528 | 8% | -16.9% | -20 to -14 | -8957 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 21 | 33% | -26.6% | -47 to -7 | -559 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (428, 15%) | -17% (528, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| wide_sl50_tp100 | -56% (428, 17%) | -17% (528, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| sl30_tp50 | -57% (428, 19%) | -17% (528, 8%) | -22% (4, 25%) | -27% (21, 33%) |
| sl50_tp50 | -57% (428, 21%) | -17% (528, 9%) | -22% (4, 25%) | -27% (21, 33%) |
| no_stop_tp100 | -55% (428, 18%) | -18% (528, 8%) | -13% (4, 25%) | -27% (21, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16611. Outcomes:

- missed_window: 11002
- low_liquidity: 3158
- proven_liquidity_gone: 1013
- no_momentum: 581
- research_failed: 455
- simulated failed buy: 183
- proven_low_volume: 153
- proven_price_collapsed_or_parabolic: 26
- proven: 22
- proven_no_uptrend: 12
- dip: 4
- research_passed: 2

Warning: 125 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
