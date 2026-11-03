# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T02:38:39Z. Bankroll cash (research-selected trades): 898.5. Open positions: 24. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 215 | 15% | -51.6% | -59 to -43 | -11108 |
| all momentum | 216 | 15% | -51.8% | -60 to -43 | -11209 |
| control | 237 | 8% | -16.7% | -22 to -12 | -3989 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 3 | 0% | -100.0% | - | -300 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (195, 16%) | -17% (237, 8%) | - | -100% (3, 0%) |
| wide_sl50_tp100 | -54% (195, 17%) | -17% (237, 8%) | - | -100% (3, 0%) |
| sl30_tp50 | -55% (195, 19%) | -18% (237, 9%) | - | -100% (3, 0%) |
| sl50_tp50 | -54% (195, 22%) | -18% (237, 9%) | - | -100% (3, 0%) |
| no_stop_tp100 | -54% (195, 17%) | -17% (237, 8%) | - | -100% (3, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8521. Outcomes:

- missed_window: 5653
- low_liquidity: 1914
- no_momentum: 295
- proven_liquidity_gone: 275
- research_failed: 224
- simulated failed buy: 84
- proven_low_volume: 56
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1

Warning: 57 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
