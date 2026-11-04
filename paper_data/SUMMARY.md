# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T03:28:10Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 71.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 404 | 15% | -54.5% | -60 to -48 | -22053 |
| all momentum | 406 | 15% | -54.6% | -61 to -48 | -22193 |
| control | 478 | 8% | -16.2% | -19 to -13 | -7809 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (385, 15%) | -16% (478, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -56% (385, 17%) | -17% (478, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (385, 19%) | -17% (478, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (385, 21%) | -17% (478, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (385, 17%) | -17% (478, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15098. Outcomes:

- missed_window: 9989
- low_liquidity: 2924
- proven_liquidity_gone: 871
- no_momentum: 531
- research_failed: 414
- simulated failed buy: 166
- proven_low_volume: 147
- proven_price_collapsed_or_parabolic: 21
- proven: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 115 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
