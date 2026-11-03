# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T04:34:39Z. Bankroll cash (research-selected trades): 898.0. Open positions: 13. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 231 | 16% | -50.8% | -59 to -42 | -11763 |
| all momentum | 232 | 16% | -51.0% | -59 to -43 | -11865 |
| control | 261 | 9% | -16.0% | -21 to -12 | -4202 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -52% (211, 17%) | -16% (261, 9%) | 58% (1, 100%) | -100% (4, 0%) |
| wide_sl50_tp100 | -53% (211, 18%) | -17% (261, 9%) | 58% (1, 100%) | -100% (4, 0%) |
| sl30_tp50 | -55% (211, 20%) | -17% (261, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| sl50_tp50 | -54% (211, 22%) | -17% (261, 10%) | 24% (1, 100%) | -100% (4, 0%) |
| no_stop_tp100 | -53% (211, 18%) | -17% (261, 9%) | 58% (1, 100%) | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9032. Outcomes:

- missed_window: 5989
- low_liquidity: 1992
- proven_liquidity_gone: 329
- no_momentum: 309
- research_failed: 239
- simulated failed buy: 91
- proven_low_volume: 61
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 6
- proven: 5
- research_passed: 1
- dip: 1

Warning: 60 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
