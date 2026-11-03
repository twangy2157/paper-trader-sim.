# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T16:58:11Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 18. Pools on watchlist: 70.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 335 | 14% | -55.1% | -62 to -48 | -18473 |
| all momentum | 337 | 14% | -55.1% | -62 to -48 | -18613 |
| control | 378 | 8% | -16.0% | -20 to -12 | -6093 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 15 | 33% | -36.8% | -64 to -10 | -553 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (316, 15%) | -16% (378, 8%) | 24% (2, 50%) | -37% (15, 33%) |
| wide_sl50_tp100 | -56% (316, 16%) | -16% (378, 9%) | 24% (2, 50%) | -37% (15, 33%) |
| sl30_tp50 | -57% (316, 19%) | -17% (378, 9%) | 7% (2, 50%) | -37% (15, 33%) |
| sl50_tp50 | -56% (316, 22%) | -17% (378, 10%) | 7% (2, 50%) | -37% (15, 33%) |
| no_stop_tp100 | -56% (316, 17%) | -16% (378, 9%) | 24% (2, 50%) | -37% (15, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12296. Outcomes:

- missed_window: 8164
- low_liquidity: 2466
- proven_liquidity_gone: 620
- no_momentum: 428
- research_failed: 345
- simulated failed buy: 125
- proven_low_volume: 101
- proven_price_collapsed_or_parabolic: 17
- proven: 16
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 82 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
