# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T00:21:44Z. Bankroll cash (research-selected trades): 898.5. Open positions: 27. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 201 | 15% | -51.8% | -60 to -43 | -10427 |
| all momentum | 202 | 15% | -52.0% | -60 to -43 | -10529 |
| control | 213 | 9% | -15.4% | -21 to -10 | -3290 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 3 | 0% | -100.0% | - | -300 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (181, 16%) | -15% (213, 9%) | - | -100% (3, 0%) |
| wide_sl50_tp100 | -54% (181, 17%) | -16% (213, 9%) | - | -100% (3, 0%) |
| sl30_tp50 | -55% (181, 20%) | -17% (213, 10%) | - | -100% (3, 0%) |
| sl50_tp50 | -54% (181, 22%) | -17% (213, 10%) | - | -100% (3, 0%) |
| no_stop_tp100 | -54% (181, 18%) | -16% (213, 9%) | - | -100% (3, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7916. Outcomes:

- missed_window: 5243
- low_liquidity: 1829
- no_momentum: 274
- proven_liquidity_gone: 222
- research_failed: 210
- simulated failed buy: 75
- proven_low_volume: 46
- proven_price_collapsed_or_parabolic: 7
- proven_no_uptrend: 5
- proven: 4
- research_passed: 1

Warning: 53 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
