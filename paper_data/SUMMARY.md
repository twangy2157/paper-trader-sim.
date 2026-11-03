# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T19:18:32Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 24. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 357 | 15% | -53.8% | -61 to -47 | -19253 |
| all momentum | 359 | 15% | -53.9% | -60 to -48 | -19392 |
| control | 393 | 8% | -16.2% | -20 to -13 | -6408 |
| dip buy | 3 | 33% | 12.5% | - | 37 |
| proven pools | 16 | 31% | -35.0% | -61 to -11 | -560 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (338, 15%) | -16% (393, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| wide_sl50_tp100 | -55% (338, 17%) | -16% (393, 8%) | 12% (3, 33%) | -35% (16, 31%) |
| sl30_tp50 | -56% (338, 20%) | -17% (393, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| sl50_tp50 | -56% (338, 22%) | -17% (393, 9%) | 1% (3, 33%) | -35% (16, 31%) |
| no_stop_tp100 | -55% (338, 18%) | -17% (393, 8%) | 12% (3, 33%) | -35% (16, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12947. Outcomes:

- missed_window: 8601
- low_liquidity: 2559
- proven_liquidity_gone: 677
- no_momentum: 459
- research_failed: 358
- simulated failed buy: 133
- proven_low_volume: 111
- proven: 17
- proven_price_collapsed_or_parabolic: 17
- proven_no_uptrend: 10
- dip: 3
- research_passed: 2

Warning: 87 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
