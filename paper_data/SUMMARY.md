# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T07:40:00Z. Bankroll cash (research-selected trades): 898.0. Open positions: 11. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 255 | 16% | -50.7% | -59 to -43 | -12950 |
| all momentum | 256 | 16% | -50.9% | -58 to -43 | -13052 |
| control | 289 | 9% | -16.3% | -20 to -12 | -4722 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 5 | 20% | -79.4% | - | -397 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -52% (235, 17%) | -16% (289, 9%) | 58% (1, 100%) | -79% (5, 20%) |
| wide_sl50_tp100 | -53% (235, 18%) | -17% (289, 9%) | 58% (1, 100%) | -79% (5, 20%) |
| sl30_tp50 | -54% (235, 21%) | -18% (289, 9%) | 24% (1, 100%) | -79% (5, 20%) |
| sl50_tp50 | -53% (235, 23%) | -17% (289, 10%) | 24% (1, 100%) | -79% (5, 20%) |
| no_stop_tp100 | -53% (235, 18%) | -17% (289, 9%) | 58% (1, 100%) | -79% (5, 20%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9774. Outcomes:

- missed_window: 6478
- low_liquidity: 2109
- proven_liquidity_gone: 394
- no_momentum: 336
- research_failed: 259
- simulated failed buy: 99
- proven_low_volume: 68
- proven_price_collapsed_or_parabolic: 11
- proven: 9
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 64 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
