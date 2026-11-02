# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T23:49:53Z. Bankroll cash (research-selected trades): 898.5. Open positions: 18. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 200 | 15% | -51.6% | -60 to -42 | -10327 |
| all momentum | 201 | 15% | -51.8% | -60 to -43 | -10429 |
| control | 209 | 10% | -15.5% | -21 to -10 | -3259 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 3 | 0% | -100.0% | - | -300 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (180, 16%) | -16% (209, 10%) | - | -100% (3, 0%) |
| wide_sl50_tp100 | -54% (180, 17%) | -16% (209, 10%) | - | -100% (3, 0%) |
| sl30_tp50 | -55% (180, 20%) | -17% (209, 10%) | - | -100% (3, 0%) |
| sl50_tp50 | -54% (180, 22%) | -17% (209, 11%) | - | -100% (3, 0%) |
| no_stop_tp100 | -54% (180, 18%) | -16% (209, 10%) | - | -100% (3, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7772. Outcomes:

- missed_window: 5171
- low_liquidity: 1794
- no_momentum: 266
- proven_liquidity_gone: 213
- research_failed: 204
- simulated failed buy: 71
- proven_low_volume: 38
- proven_no_uptrend: 5
- proven_price_collapsed_or_parabolic: 5
- proven: 4
- research_passed: 1

Warning: 48 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
