# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T13:17:10Z. Bankroll cash (research-selected trades): 898.0. Open positions: 14. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 306 | 14% | -54.3% | -61 to -47 | -16631 |
| all momentum | 307 | 14% | -54.4% | -61 to -47 | -16733 |
| control | 341 | 8% | -17.0% | -21 to -13 | -5835 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 11 | 36% | -41.8% | -73 to -11 | -461 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (286, 15%) | -17% (341, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| wide_sl50_tp100 | -56% (286, 17%) | -17% (341, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| sl30_tp50 | -57% (286, 19%) | -18% (341, 8%) | 7% (2, 50%) | -42% (11, 36%) |
| sl50_tp50 | -56% (286, 22%) | -18% (341, 9%) | 7% (2, 50%) | -42% (11, 36%) |
| no_stop_tp100 | -56% (286, 17%) | -17% (341, 8%) | 24% (2, 50%) | -42% (11, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11168. Outcomes:

- missed_window: 7388
- low_liquidity: 2308
- proven_liquidity_gone: 525
- no_momentum: 388
- research_failed: 313
- simulated failed buy: 114
- proven_low_volume: 92
- proven: 15
- proven_price_collapsed_or_parabolic: 13
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 73 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
