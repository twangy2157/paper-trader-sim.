# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T05:27:33Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 23. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 422 | 15% | -54.4% | -61 to -48 | -22978 |
| all momentum | 424 | 15% | -54.4% | -60 to -49 | -23118 |
| control | 493 | 8% | -16.4% | -20 to -13 | -8138 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (403, 15%) | -16% (493, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (403, 17%) | -17% (493, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (403, 19%) | -17% (493, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (403, 21%) | -17% (493, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (403, 18%) | -17% (493, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15778. Outcomes:

- missed_window: 10469
- low_liquidity: 3022
- proven_liquidity_gone: 924
- no_momentum: 553
- research_failed: 427
- simulated failed buy: 174
- proven_low_volume: 150
- proven_price_collapsed_or_parabolic: 22
- proven: 21
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 120 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
