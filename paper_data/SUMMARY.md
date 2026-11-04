# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T03:16:42Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 16.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 403 | 15% | -54.6% | -61 to -48 | -22049 |
| all momentum | 405 | 15% | -54.7% | -61 to -49 | -22189 |
| control | 476 | 8% | -16.4% | -20 to -13 | -7861 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (384, 15%) | -16% (476, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -56% (384, 17%) | -17% (476, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (384, 19%) | -17% (476, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -57% (384, 21%) | -17% (476, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (384, 17%) | -17% (476, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15071. Outcomes:

- missed_window: 9982
- low_liquidity: 2915
- proven_liquidity_gone: 863
- no_momentum: 529
- research_failed: 413
- simulated failed buy: 166
- proven_low_volume: 147
- proven_price_collapsed_or_parabolic: 21
- proven: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 115 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
