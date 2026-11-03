# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T12:05:11Z. Bankroll cash (research-selected trades): 898.0. Open positions: 19. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 293 | 15% | -53.1% | -60 to -46 | -15596 |
| all momentum | 294 | 15% | -53.3% | -60 to -46 | -15698 |
| control | 334 | 8% | -17.0% | -21 to -13 | -5695 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 11 | 36% | -41.8% | -73 to -11 | -461 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (273, 16%) | -17% (334, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| wide_sl50_tp100 | -55% (273, 17%) | -17% (334, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| sl30_tp50 | -56% (273, 20%) | -18% (334, 8%) | 7% (2, 50%) | -42% (11, 36%) |
| sl50_tp50 | -55% (273, 22%) | -18% (334, 9%) | 7% (2, 50%) | -42% (11, 36%) |
| no_stop_tp100 | -55% (273, 18%) | -17% (334, 8%) | 24% (2, 50%) | -42% (11, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10920. Outcomes:

- missed_window: 7225
- low_liquidity: 2272
- proven_liquidity_gone: 500
- no_momentum: 385
- research_failed: 302
- simulated failed buy: 111
- proven_low_volume: 86
- proven: 14
- proven_price_collapsed_or_parabolic: 13
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 71 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
