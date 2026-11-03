# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T08:35:32Z. Bankroll cash (research-selected trades): 898.0. Open positions: 31. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 258 | 16% | -50.5% | -58 to -42 | -13057 |
| all momentum | 259 | 16% | -50.7% | -59 to -43 | -13159 |
| control | 290 | 9% | -16.2% | -21 to -12 | -4729 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 6 | 33% | -65.7% | -100 to -31 | -395 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -52% (238, 17%) | -16% (290, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| wide_sl50_tp100 | -52% (238, 18%) | -17% (290, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| sl30_tp50 | -54% (238, 21%) | -18% (290, 9%) | 24% (1, 100%) | -66% (6, 33%) |
| sl50_tp50 | -53% (238, 23%) | -17% (290, 10%) | 24% (1, 100%) | -66% (6, 33%) |
| no_stop_tp100 | -53% (238, 18%) | -17% (290, 9%) | 58% (1, 100%) | -66% (6, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9995. Outcomes:

- missed_window: 6593
- low_liquidity: 2158
- proven_liquidity_gone: 419
- no_momentum: 345
- research_failed: 273
- simulated failed buy: 101
- proven_low_volume: 72
- proven_price_collapsed_or_parabolic: 12
- proven: 11
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 65 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
