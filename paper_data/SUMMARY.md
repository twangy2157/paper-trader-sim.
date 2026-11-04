# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T08:27:20Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 26. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 437 | 15% | -54.1% | -60 to -48 | -23686 |
| all momentum | 439 | 15% | -54.2% | -60 to -48 | -23826 |
| control | 519 | 8% | -16.7% | -20 to -14 | -8718 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 21 | 33% | -26.6% | -47 to -7 | -559 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (418, 16%) | -17% (519, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| wide_sl50_tp100 | -55% (418, 17%) | -17% (519, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| sl30_tp50 | -57% (418, 19%) | -17% (519, 8%) | -22% (4, 25%) | -27% (21, 33%) |
| sl50_tp50 | -56% (418, 21%) | -17% (519, 9%) | -22% (4, 25%) | -27% (21, 33%) |
| no_stop_tp100 | -55% (418, 18%) | -17% (519, 8%) | -13% (4, 25%) | -27% (21, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16447. Outcomes:

- missed_window: 10893
- low_liquidity: 3124
- proven_liquidity_gone: 1005
- no_momentum: 575
- research_failed: 450
- simulated failed buy: 181
- proven_low_volume: 153
- proven_price_collapsed_or_parabolic: 26
- proven: 22
- proven_no_uptrend: 12
- dip: 4
- research_passed: 2

Warning: 124 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
