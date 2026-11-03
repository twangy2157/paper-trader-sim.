# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T08:46:43Z. Bankroll cash (research-selected trades): 898.0. Open positions: 33. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 260 | 16% | -50.9% | -58 to -42 | -13257 |
| all momentum | 261 | 16% | -51.1% | -58 to -43 | -13359 |
| control | 292 | 9% | -16.2% | -21 to -12 | -4749 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 6 | 33% | -65.7% | -100 to -31 | -395 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -52% (240, 17%) | -16% (292, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| wide_sl50_tp100 | -53% (240, 18%) | -17% (292, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| sl30_tp50 | -54% (240, 21%) | -17% (292, 9%) | 24% (1, 100%) | -66% (6, 33%) |
| sl50_tp50 | -53% (240, 23%) | -17% (292, 10%) | 24% (1, 100%) | -66% (6, 33%) |
| no_stop_tp100 | -53% (240, 18%) | -17% (292, 9%) | 58% (1, 100%) | -66% (6, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10039. Outcomes:

- missed_window: 6625
- low_liquidity: 2163
- proven_liquidity_gone: 419
- no_momentum: 346
- research_failed: 278
- simulated failed buy: 102
- proven_low_volume: 72
- proven_price_collapsed_or_parabolic: 12
- proven: 11
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 66 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
