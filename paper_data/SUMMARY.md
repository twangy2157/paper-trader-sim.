# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T10:12:43Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 20. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 455 | 15% | -54.4% | -60 to -49 | -24808 |
| all momentum | 457 | 15% | -54.5% | -60 to -49 | -24948 |
| control | 537 | 8% | -17.1% | -20 to -14 | -9243 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 21 | 33% | -26.6% | -47 to -7 | -559 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (436, 16%) | -17% (537, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| wide_sl50_tp100 | -55% (436, 17%) | -18% (537, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| sl30_tp50 | -57% (436, 19%) | -18% (537, 8%) | -22% (4, 25%) | -27% (21, 33%) |
| sl50_tp50 | -56% (436, 21%) | -18% (537, 9%) | -22% (4, 25%) | -27% (21, 33%) |
| no_stop_tp100 | -55% (436, 18%) | -18% (537, 8%) | -13% (4, 25%) | -27% (21, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16909. Outcomes:

- missed_window: 11195
- low_liquidity: 3204
- proven_liquidity_gone: 1041
- no_momentum: 590
- research_failed: 463
- simulated failed buy: 187
- proven_low_volume: 160
- proven_price_collapsed_or_parabolic: 27
- proven: 24
- proven_no_uptrend: 12
- dip: 4
- research_passed: 2

Warning: 129 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
