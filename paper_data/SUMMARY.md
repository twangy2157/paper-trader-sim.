# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T12:38:38Z. Bankroll cash (research-selected trades): 898.0. Open positions: 16. Pools on watchlist: 34.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 300 | 15% | -53.6% | -61 to -46 | -16097 |
| all momentum | 301 | 15% | -53.7% | -61 to -46 | -16199 |
| control | 338 | 8% | -17.1% | -21 to -13 | -5817 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 11 | 36% | -41.8% | -73 to -11 | -461 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (280, 15%) | -17% (338, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| wide_sl50_tp100 | -55% (280, 17%) | -18% (338, 8%) | 24% (2, 50%) | -42% (11, 36%) |
| sl30_tp50 | -56% (280, 20%) | -18% (338, 8%) | 7% (2, 50%) | -42% (11, 36%) |
| sl50_tp50 | -55% (280, 22%) | -18% (338, 9%) | 7% (2, 50%) | -42% (11, 36%) |
| no_stop_tp100 | -55% (280, 18%) | -18% (338, 8%) | 24% (2, 50%) | -42% (11, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 11077. Outcomes:

- missed_window: 7324
- low_liquidity: 2299
- proven_liquidity_gone: 517
- no_momentum: 386
- research_failed: 309
- simulated failed buy: 113
- proven_low_volume: 90
- proven: 14
- proven_price_collapsed_or_parabolic: 13
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 73 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
