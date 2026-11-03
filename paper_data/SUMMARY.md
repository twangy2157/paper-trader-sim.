# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T13:05:40Z. Bankroll cash (research-selected trades): 898.0. Open positions: 15. Pools on watchlist: 39.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 302 | 15% | -53.7% | -61 to -46 | -16231 |
| all momentum | 303 | 15% | -53.8% | -61 to -47 | -16333 |
| control | 340 | 8% | -17.1% | -21 to -13 | -5831 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 11 | 36% | -41.8% | -73 to -11 | -461 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (282, 15%) | -17% (340, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| wide_sl50_tp100 | -55% (282, 17%) | -17% (340, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| sl30_tp50 | -56% (282, 20%) | -18% (340, 8%) | 7% (2, 50%) | -42% (11, 36%) |
| sl50_tp50 | -55% (282, 22%) | -18% (340, 9%) | 7% (2, 50%) | -42% (11, 36%) |
| no_stop_tp100 | -55% (282, 18%) | -17% (340, 8%) | 24% (2, 50%) | -42% (11, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11125. Outcomes:

- missed_window: 7358
- low_liquidity: 2304
- proven_liquidity_gone: 521
- no_momentum: 388
- research_failed: 310
- simulated failed buy: 114
- proven_low_volume: 91
- proven: 14
- proven_price_collapsed_or_parabolic: 13
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 73 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
