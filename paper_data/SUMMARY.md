# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T18:56:11Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 17. Pools on watchlist: 68.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 354 | 15% | -53.5% | -60 to -46 | -18953 |
| all momentum | 356 | 15% | -53.5% | -60 to -47 | -19093 |
| control | 390 | 8% | -16.3% | -20 to -13 | -6383 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 16 | 31% | -35.0% | -61 to -11 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (335, 16%) | -16% (390, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| wide_sl50_tp100 | -55% (335, 17%) | -17% (390, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| sl30_tp50 | -56% (335, 20%) | -17% (390, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| sl50_tp50 | -55% (335, 22%) | -17% (390, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| no_stop_tp100 | -55% (335, 18%) | -17% (390, 8%) | 12% (3, 33%) | -35% (16, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12835. Outcomes:

- missed_window: 8527
- low_liquidity: 2547
- proven_liquidity_gone: 668
- no_momentum: 447
- research_failed: 357
- simulated failed buy: 132
- proven_low_volume: 109
- proven: 17
- proven_price_collapsed_or_parabolic: 17
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 86 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
