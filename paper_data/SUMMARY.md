# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T16:47:53Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 16. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 333 | 14% | -54.8% | -61 to -48 | -18273 |
| all momentum | 335 | 14% | -54.9% | -61 to -48 | -18413 |
| control | 376 | 8% | -16.2% | -20 to -13 | -6113 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 15 | 33% | -36.8% | -64 to -10 | -553 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (314, 15%) | -16% (376, 8%) | 24% (2, 50%) | -37% (15, 33%) |
| wide_sl50_tp100 | -56% (314, 17%) | -16% (376, 9%) | 24% (2, 50%) | -37% (15, 33%) |
| sl30_tp50 | -57% (314, 19%) | -17% (376, 9%) | 7% (2, 50%) | -37% (15, 33%) |
| sl50_tp50 | -56% (314, 22%) | -17% (376, 9%) | 7% (2, 50%) | -37% (15, 33%) |
| no_stop_tp100 | -56% (314, 17%) | -17% (376, 9%) | 24% (2, 50%) | -37% (15, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12267. Outcomes:

- missed_window: 8147
- low_liquidity: 2460
- proven_liquidity_gone: 620
- no_momentum: 427
- research_failed: 340
- simulated failed buy: 125
- proven_low_volume: 101
- proven_price_collapsed_or_parabolic: 17
- proven: 16
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 82 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
