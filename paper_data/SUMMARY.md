# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T03:21:31Z. Bankroll cash (research-selected trades): 898.5. Open positions: 18. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 222 | 15% | -51.7% | -60 to -43 | -11499 |
| all momentum | 223 | 15% | -51.9% | -60 to -43 | -11600 |
| control | 250 | 8% | -16.3% | -21 to -12 | -4096 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (202, 16%) | -16% (250, 8%) | - | -100% (4, 0%) |
| wide_sl50_tp100 | -54% (202, 17%) | -17% (250, 8%) | - | -100% (4, 0%) |
| sl30_tp50 | -55% (202, 19%) | -18% (250, 9%) | - | -100% (4, 0%) |
| sl50_tp50 | -55% (202, 21%) | -18% (250, 9%) | - | -100% (4, 0%) |
| no_stop_tp100 | -54% (202, 17%) | -17% (250, 8%) | - | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8700. Outcomes:

- missed_window: 5780
- low_liquidity: 1934
- no_momentum: 303
- proven_liquidity_gone: 285
- research_failed: 230
- simulated failed buy: 88
- proven_low_volume: 59
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1
- dip: 1

Warning: 59 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
