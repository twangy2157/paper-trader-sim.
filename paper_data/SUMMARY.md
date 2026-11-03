# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T19:07:43Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 20. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 355 | 15% | -53.6% | -60 to -47 | -19053 |
| all momentum | 357 | 15% | -53.7% | -60 to -47 | -19193 |
| control | 391 | 8% | -16.3% | -20 to -13 | -6392 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 16 | 31% | -35.0% | -61 to -11 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (336, 15%) | -16% (391, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| wide_sl50_tp100 | -55% (336, 17%) | -17% (391, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| sl30_tp50 | -56% (336, 20%) | -17% (391, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| sl50_tp50 | -55% (336, 22%) | -17% (391, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| no_stop_tp100 | -55% (336, 18%) | -17% (391, 8%) | 12% (3, 33%) | -35% (16, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12897. Outcomes:

- missed_window: 8568
- low_liquidity: 2556
- proven_liquidity_gone: 674
- no_momentum: 452
- research_failed: 357
- simulated failed buy: 133
- proven_low_volume: 109
- proven: 17
- proven_price_collapsed_or_parabolic: 17
- proven_no_uptrend: 9
- dip: 3
- research_passed: 2

Warning: 87 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
