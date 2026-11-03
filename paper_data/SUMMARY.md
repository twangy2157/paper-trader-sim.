# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T08:58:00Z. Bankroll cash (research-selected trades): 898.0. Open positions: 30. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 265 | 15% | -51.8% | -59 to -44 | -13758 |
| all momentum | 266 | 15% | -52.0% | -59 to -44 | -13860 |
| control | 294 | 9% | -16.1% | -20 to -12 | -4750 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 6 | 33% | -65.7% | -100 to -31 | -395 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (245, 16%) | -16% (294, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| wide_sl50_tp100 | -54% (245, 18%) | -17% (294, 9%) | 58% (1, 100%) | -66% (6, 33%) |
| sl30_tp50 | -55% (245, 20%) | -17% (294, 9%) | 24% (1, 100%) | -66% (6, 33%) |
| sl50_tp50 | -54% (245, 22%) | -17% (294, 10%) | 24% (1, 100%) | -66% (6, 33%) |
| no_stop_tp100 | -54% (245, 18%) | -17% (294, 9%) | 58% (1, 100%) | -66% (6, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 10079. Outcomes:

- missed_window: 6653
- low_liquidity: 2169
- proven_liquidity_gone: 420
- no_momentum: 348
- research_failed: 280
- simulated failed buy: 103
- proven_low_volume: 72
- proven_price_collapsed_or_parabolic: 12
- proven: 11
- proven_no_uptrend: 9
- research_passed: 1
- dip: 1

Warning: 67 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
