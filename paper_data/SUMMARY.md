# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T08:02:39Z. Bankroll cash (research-selected trades): 898.0. Open positions: 20. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 255 | 16% | -50.7% | -59 to -43 | -12950 |
| all momentum | 256 | 16% | -50.9% | -58 to -43 | -13052 |
| control | 289 | 9% | -16.3% | -20 to -12 | -4723 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 6 | 33% | -65.7% | -100 to -31 | -395 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -52% (235, 17%) | -16% (289, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| wide_sl50_tp100 | -53% (235, 18%) | -17% (289, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| sl30_tp50 | -54% (235, 21%) | -18% (289, 9%) | 24% (1, 100%) | -66% (6, 33%) |
| sl50_tp50 | -53% (235, 23%) | -17% (289, 10%) | 24% (1, 100%) | -66% (6, 33%) |
| no_stop_tp100 | -53% (235, 18%) | -17% (289, 9%) | 58% (1, 100%) | -66% (6, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9859. Outcomes:

- missed_window: 6519
- low_liquidity: 2128
- proven_liquidity_gone: 404
- no_momentum: 338
- research_failed: 266
- simulated failed buy: 100
- proven_low_volume: 71
- proven_price_collapsed_or_parabolic: 12
- proven: 10
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 65 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
