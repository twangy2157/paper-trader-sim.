# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T10:33:33Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 17. Pools on watchlist: 32.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 460 | 15% | -54.4% | -60 to -49 | -25050 |
| all momentum | 462 | 15% | -54.4% | -60 to -49 | -25190 |
| control | 540 | 8% | -17.3% | -20 to -14 | -9370 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 21 | 33% | -26.6% | -47 to -7 | -559 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (441, 16%) | -17% (540, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| wide_sl50_tp100 | -55% (441, 17%) | -18% (540, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| sl30_tp50 | -57% (441, 19%) | -18% (540, 8%) | -22% (4, 25%) | -27% (21, 33%) |
| sl50_tp50 | -56% (441, 21%) | -18% (540, 9%) | -22% (4, 25%) | -27% (21, 33%) |
| no_stop_tp100 | -55% (441, 18%) | -18% (540, 8%) | -13% (4, 25%) | -27% (21, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16987. Outcomes:

- missed_window: 11239
- low_liquidity: 3217
- proven_liquidity_gone: 1053
- no_momentum: 594
- research_failed: 464
- simulated failed buy: 190
- proven_low_volume: 161
- proven_price_collapsed_or_parabolic: 27
- proven: 24
- proven_no_uptrend: 12
- dip: 4
- research_passed: 2

Warning: 130 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
