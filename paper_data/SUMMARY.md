# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T12:25:35Z. Bankroll cash (research-selected trades): 898.0. Open positions: 17. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 298 | 15% | -53.6% | -61 to -46 | -15994 |
| all momentum | 299 | 15% | -53.7% | -61 to -46 | -16096 |
| control | 336 | 8% | -16.9% | -21 to -13 | -5706 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 11 | 36% | -41.8% | -73 to -11 | -461 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (278, 15%) | -17% (336, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| wide_sl50_tp100 | -55% (278, 17%) | -17% (336, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| sl30_tp50 | -56% (278, 20%) | -18% (336, 8%) | 7% (2, 50%) | -42% (11, 36%) |
| sl50_tp50 | -55% (278, 22%) | -18% (336, 9%) | 7% (2, 50%) | -42% (11, 36%) |
| no_stop_tp100 | -55% (278, 18%) | -17% (336, 8%) | 24% (2, 50%) | -42% (11, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11005. Outcomes:

- missed_window: 7275
- low_liquidity: 2289
- proven_liquidity_gone: 511
- no_momentum: 386
- research_failed: 306
- simulated failed buy: 111
- proven_low_volume: 88
- proven: 14
- proven_price_collapsed_or_parabolic: 13
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 71 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
