# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T16:17:10Z. Bankroll cash (research-selected trades): 798.0. Open positions: 26. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 329 | 14% | -54.4% | -61 to -48 | -17938 |
| all momentum | 330 | 14% | -54.6% | -61 to -48 | -18040 |
| control | 366 | 8% | -16.2% | -20 to -12 | -5953 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 15 | 33% | -36.8% | -64 to -10 | -553 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (309, 15%) | -16% (366, 8%) | 24% (2, 50%) | -37% (15, 33%) |
| wide_sl50_tp100 | -55% (309, 17%) | -16% (366, 8%) | 24% (2, 50%) | -37% (15, 33%) |
| sl30_tp50 | -57% (309, 19%) | -17% (366, 9%) | 7% (2, 50%) | -37% (15, 33%) |
| sl50_tp50 | -56% (309, 22%) | -17% (366, 9%) | 7% (2, 50%) | -37% (15, 33%) |
| no_stop_tp100 | -55% (309, 17%) | -17% (366, 8%) | 24% (2, 50%) | -37% (15, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12102. Outcomes:

- missed_window: 8026
- low_liquidity: 2441
- proven_liquidity_gone: 604
- no_momentum: 425
- research_failed: 337
- simulated failed buy: 123
- proven_low_volume: 100
- proven: 16
- proven_price_collapsed_or_parabolic: 16
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 80 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
