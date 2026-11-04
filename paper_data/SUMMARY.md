# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T09:19:00Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 448 | 15% | -54.3% | -60 to -49 | -24372 |
| all momentum | 450 | 15% | -54.4% | -60 to -49 | -24512 |
| control | 530 | 8% | -17.1% | -20 to -14 | -9093 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 21 | 33% | -26.6% | -47 to -7 | -559 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (429, 16%) | -17% (530, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| wide_sl50_tp100 | -55% (429, 17%) | -17% (530, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| sl30_tp50 | -57% (429, 19%) | -18% (530, 8%) | -22% (4, 25%) | -27% (21, 33%) |
| sl50_tp50 | -56% (429, 21%) | -18% (530, 9%) | -22% (4, 25%) | -27% (21, 33%) |
| no_stop_tp100 | -55% (429, 18%) | -18% (530, 8%) | -13% (4, 25%) | -27% (21, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16659. Outcomes:

- missed_window: 11034
- low_liquidity: 3163
- proven_liquidity_gone: 1019
- no_momentum: 583
- research_failed: 457
- simulated failed buy: 183
- proven_low_volume: 154
- proven_price_collapsed_or_parabolic: 26
- proven: 22
- proven_no_uptrend: 12
- dip: 4
- research_passed: 2

Warning: 126 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
