# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T10:01:29Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 18. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 455 | 15% | -54.4% | -60 to -49 | -24808 |
| all momentum | 457 | 15% | -54.5% | -60 to -49 | -24948 |
| control | 536 | 8% | -17.1% | -20 to -14 | -9234 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 21 | 33% | -26.6% | -47 to -7 | -559 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (436, 16%) | -17% (536, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| wide_sl50_tp100 | -55% (436, 17%) | -18% (536, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| sl30_tp50 | -57% (436, 19%) | -18% (536, 8%) | -22% (4, 25%) | -27% (21, 33%) |
| sl50_tp50 | -56% (436, 21%) | -18% (536, 9%) | -22% (4, 25%) | -27% (21, 33%) |
| no_stop_tp100 | -55% (436, 18%) | -18% (536, 8%) | -13% (4, 25%) | -27% (21, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16859. Outcomes:

- missed_window: 11166
- low_liquidity: 3195
- proven_liquidity_gone: 1036
- no_momentum: 588
- research_failed: 463
- simulated failed buy: 185
- proven_low_volume: 159
- proven_price_collapsed_or_parabolic: 26
- proven: 23
- proven_no_uptrend: 12
- dip: 4
- research_passed: 2

Warning: 127 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
