# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T08:47:39Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 27. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 440 | 15% | -54.2% | -60 to -48 | -23874 |
| all momentum | 442 | 15% | -54.2% | -60 to -48 | -24014 |
| control | 522 | 8% | -16.6% | -20 to -14 | -8733 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 21 | 33% | -26.6% | -47 to -7 | -559 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (421, 15%) | -17% (522, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| wide_sl50_tp100 | -55% (421, 17%) | -17% (522, 8%) | -13% (4, 25%) | -27% (21, 33%) |
| sl30_tp50 | -57% (421, 19%) | -17% (522, 8%) | -22% (4, 25%) | -27% (21, 33%) |
| sl50_tp50 | -56% (421, 21%) | -17% (522, 9%) | -22% (4, 25%) | -27% (21, 33%) |
| no_stop_tp100 | -55% (421, 18%) | -17% (522, 8%) | -13% (4, 25%) | -27% (21, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16527. Outcomes:

- missed_window: 10939
- low_liquidity: 3143
- proven_liquidity_gone: 1011
- no_momentum: 578
- research_failed: 454
- simulated failed buy: 183
- proven_low_volume: 153
- proven_price_collapsed_or_parabolic: 26
- proven: 22
- proven_no_uptrend: 12
- dip: 4
- research_passed: 2

Warning: 125 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
