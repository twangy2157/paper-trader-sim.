# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T05:17:11Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 21. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 421 | 15% | -54.5% | -61 to -48 | -22974 |
| all momentum | 423 | 15% | -54.6% | -61 to -48 | -23114 |
| control | 492 | 8% | -16.4% | -20 to -13 | -8124 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (402, 15%) | -16% (492, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (402, 17%) | -17% (492, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (402, 19%) | -17% (492, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -57% (402, 21%) | -17% (492, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (402, 18%) | -17% (492, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15713. Outcomes:

- missed_window: 10425
- low_liquidity: 3013
- proven_liquidity_gone: 917
- no_momentum: 551
- research_failed: 425
- simulated failed buy: 173
- proven_low_volume: 150
- proven_price_collapsed_or_parabolic: 22
- proven: 21
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 119 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
