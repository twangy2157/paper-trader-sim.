# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T08:23:59Z. Bankroll cash (research-selected trades): 898.0. Open positions: 27. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 256 | 16% | -50.9% | -59 to -43 | -13051 |
| all momentum | 257 | 16% | -51.1% | -59 to -43 | -13153 |
| control | 290 | 9% | -16.2% | -21 to -12 | -4729 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 6 | 33% | -65.7% | -100 to -31 | -395 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -52% (236, 17%) | -16% (290, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| wide_sl50_tp100 | -53% (236, 18%) | -17% (290, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| sl30_tp50 | -54% (236, 21%) | -18% (290, 9%) | 24% (1, 100%) | -66% (6, 33%) |
| sl50_tp50 | -53% (236, 23%) | -17% (290, 10%) | 24% (1, 100%) | -66% (6, 33%) |
| no_stop_tp100 | -53% (236, 18%) | -17% (290, 9%) | 58% (1, 100%) | -66% (6, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9934. Outcomes:

- missed_window: 6552
- low_liquidity: 2149
- proven_liquidity_gone: 414
- no_momentum: 342
- research_failed: 270
- simulated failed buy: 101
- proven_low_volume: 72
- proven_price_collapsed_or_parabolic: 12
- proven: 11
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 65 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
