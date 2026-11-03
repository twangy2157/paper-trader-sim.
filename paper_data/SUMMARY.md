# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T11:21:21Z. Bankroll cash (research-selected trades): 898.0. Open positions: 32. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 283 | 15% | -52.9% | -60 to -45 | -15005 |
| all momentum | 284 | 15% | -53.1% | -60 to -46 | -15107 |
| control | 324 | 8% | -16.4% | -20 to -13 | -5351 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 11 | 36% | -41.8% | -73 to -11 | -461 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (263, 16%) | -16% (324, 8%) | 58% (1, 100%) | -42% (11, 36%) |
| wide_sl50_tp100 | -55% (263, 17%) | -17% (324, 8%) | 58% (1, 100%) | -42% (11, 36%) |
| sl30_tp50 | -56% (263, 20%) | -18% (324, 8%) | 24% (1, 100%) | -42% (11, 36%) |
| sl50_tp50 | -55% (263, 22%) | -17% (324, 9%) | 24% (1, 100%) | -42% (11, 36%) |
| no_stop_tp100 | -55% (263, 18%) | -17% (324, 8%) | 58% (1, 100%) | -42% (11, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10724. Outcomes:

- missed_window: 7086
- low_liquidity: 2247
- proven_liquidity_gone: 479
- no_momentum: 381
- research_failed: 298
- simulated failed buy: 111
- proven_low_volume: 83
- proven: 14
- proven_price_collapsed_or_parabolic: 13
- proven_no_uptrend: 9
- dip: 2
- research_passed: 1

Warning: 71 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
