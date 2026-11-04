# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T05:05:43Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 418 | 15% | -54.2% | -60 to -48 | -22674 |
| all momentum | 420 | 15% | -54.2% | -60 to -48 | -22814 |
| control | 492 | 8% | -16.4% | -20 to -13 | -8124 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (399, 16%) | -16% (492, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (399, 17%) | -17% (492, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (399, 19%) | -17% (492, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (399, 21%) | -17% (492, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (399, 18%) | -17% (492, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15653. Outcomes:

- missed_window: 10385
- low_liquidity: 3005
- proven_liquidity_gone: 912
- no_momentum: 548
- research_failed: 424
- simulated failed buy: 173
- proven_low_volume: 148
- proven_price_collapsed_or_parabolic: 22
- proven: 20
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 119 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
