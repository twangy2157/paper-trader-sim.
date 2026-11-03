# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T16:27:33Z. Bankroll cash (research-selected trades): 798.0. Open positions: 21. Pools on watchlist: 80.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 332 | 14% | -54.8% | -62 to -48 | -18238 |
| all momentum | 333 | 14% | -55.0% | -62 to -48 | -18340 |
| control | 369 | 8% | -16.3% | -20 to -13 | -6063 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 15 | 33% | -36.8% | -64 to -10 | -553 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (312, 15%) | -16% (369, 8%) | 24% (2, 50%) | -37% (15, 33%) |
| wide_sl50_tp100 | -56% (312, 17%) | -17% (369, 8%) | 24% (2, 50%) | -37% (15, 33%) |
| sl30_tp50 | -57% (312, 19%) | -17% (369, 9%) | 7% (2, 50%) | -37% (15, 33%) |
| sl50_tp50 | -56% (312, 22%) | -17% (369, 9%) | 7% (2, 50%) | -37% (15, 33%) |
| no_stop_tp100 | -56% (312, 17%) | -17% (369, 8%) | 24% (2, 50%) | -37% (15, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12151. Outcomes:

- missed_window: 8061
- low_liquidity: 2446
- proven_liquidity_gone: 609
- no_momentum: 425
- research_failed: 338
- simulated failed buy: 125
- proven_low_volume: 101
- proven: 16
- proven_price_collapsed_or_parabolic: 16
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 82 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
