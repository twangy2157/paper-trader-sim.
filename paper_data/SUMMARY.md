# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T17:08:35Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 18. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 336 | 14% | -55.2% | -61 to -48 | -18573 |
| all momentum | 338 | 14% | -55.3% | -62 to -49 | -18713 |
| control | 380 | 8% | -16.0% | -20 to -12 | -6103 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 15 | 33% | -36.8% | -64 to -10 | -553 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (317, 15%) | -16% (380, 8%) | 24% (2, 50%) | -37% (15, 33%) |
| wide_sl50_tp100 | -56% (317, 16%) | -16% (380, 9%) | 24% (2, 50%) | -37% (15, 33%) |
| sl30_tp50 | -57% (317, 19%) | -17% (380, 9%) | 7% (2, 50%) | -37% (15, 33%) |
| sl50_tp50 | -57% (317, 21%) | -17% (380, 9%) | 7% (2, 50%) | -37% (15, 33%) |
| no_stop_tp100 | -56% (317, 17%) | -16% (380, 9%) | 24% (2, 50%) | -37% (15, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12362. Outcomes:

- missed_window: 8210
- low_liquidity: 2477
- proven_liquidity_gone: 625
- no_momentum: 429
- research_failed: 347
- simulated failed buy: 125
- proven_low_volume: 102
- proven_price_collapsed_or_parabolic: 17
- proven: 16
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 82 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
