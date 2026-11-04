# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T09:40:39Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 452 | 15% | -54.1% | -60 to -48 | -24506 |
| all momentum | 454 | 15% | -54.2% | -60 to -48 | -24646 |
| control | 532 | 8% | -17.0% | -20 to -14 | -9115 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 21 | 33% | -26.6% | -47 to -7 | -559 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (433, 16%) | -17% (532, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| wide_sl50_tp100 | -55% (433, 17%) | -17% (532, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| sl30_tp50 | -56% (433, 19%) | -17% (532, 8%) | -22% (4, 25%) | -27% (21, 33%) |
| sl50_tp50 | -56% (433, 21%) | -18% (532, 9%) | -22% (4, 25%) | -27% (21, 33%) |
| no_stop_tp100 | -55% (433, 18%) | -18% (532, 8%) | -13% (4, 25%) | -27% (21, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16759. Outcomes:

- missed_window: 11098
- low_liquidity: 3178
- proven_liquidity_gone: 1029
- no_momentum: 585
- research_failed: 461
- simulated failed buy: 185
- proven_low_volume: 157
- proven_price_collapsed_or_parabolic: 26
- proven: 22
- proven_no_uptrend: 12
- dip: 4
- research_passed: 2

Warning: 127 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
