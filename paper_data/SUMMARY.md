# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T22:08:21Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 30. Pools on watchlist: 31.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 368 | 15% | -54.1% | -60 to -47 | -19947 |
| all momentum | 370 | 15% | -54.2% | -61 to -48 | -20087 |
| control | 433 | 8% | -15.9% | -19 to -13 | -6937 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 17 | 35% | -32.9% | -59 to -10 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (349, 15%) | -16% (433, 8%) | 12% (3, 33%) | -33% (17, 35%) |
| wide_sl50_tp100 | -55% (349, 17%) | -16% (433, 8%) | 12% (3, 33%) | -33% (17, 35%) |
| sl30_tp50 | -57% (349, 19%) | -17% (433, 8%) | 1% (3, 33%) | -33% (17, 35%) |
| sl50_tp50 | -56% (349, 21%) | -17% (433, 9%) | 1% (3, 33%) | -33% (17, 35%) |
| no_stop_tp100 | -55% (349, 17%) | -16% (433, 8%) | 12% (3, 33%) | -33% (17, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 13713. Outcomes:

- missed_window: 9093
- low_liquidity: 2678
- proven_liquidity_gone: 735
- no_momentum: 495
- research_failed: 378
- simulated failed buy: 145
- proven_low_volume: 137
- proven: 18
- proven_price_collapsed_or_parabolic: 18
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 95 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
