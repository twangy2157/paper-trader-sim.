# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T02:21:44Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 394 | 14% | -54.7% | -61 to -48 | -21591 |
| all momentum | 396 | 14% | -54.8% | -61 to -49 | -21731 |
| control | 469 | 7% | -16.1% | -19 to -13 | -7605 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (375, 15%) | -16% (469, 7%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -56% (375, 17%) | -17% (469, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (375, 19%) | -17% (469, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -57% (375, 21%) | -17% (469, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -56% (375, 17%) | -17% (469, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 14813. Outcomes:

- missed_window: 9814
- low_liquidity: 2861
- proven_liquidity_gone: 849
- no_momentum: 522
- research_failed: 404
- simulated failed buy: 163
- proven_low_volume: 144
- proven_price_collapsed_or_parabolic: 21
- proven: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 112 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
