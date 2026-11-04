# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T04:54:44Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 19. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 417 | 15% | -54.3% | -60 to -48 | -22669 |
| all momentum | 419 | 15% | -54.3% | -60 to -48 | -22808 |
| control | 490 | 8% | -16.3% | -19 to -13 | -8015 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (398, 16%) | -16% (490, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (398, 17%) | -17% (490, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (398, 19%) | -17% (490, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (398, 21%) | -17% (490, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (398, 18%) | -17% (490, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15576. Outcomes:

- missed_window: 10327
- low_liquidity: 2996
- proven_liquidity_gone: 906
- no_momentum: 545
- research_failed: 424
- simulated failed buy: 172
- proven_low_volume: 148
- proven_price_collapsed_or_parabolic: 22
- proven: 20
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 118 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
