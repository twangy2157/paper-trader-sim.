# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T04:45:42Z. Bankroll cash (research-selected trades): 898.0. Open positions: 12. Pools on watchlist: 105.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 233 | 15% | -51.2% | -59 to -43 | -11958 |
| all momentum | 234 | 15% | -51.4% | -60 to -43 | -12060 |
| control | 264 | 9% | -16.6% | -21 to -12 | -4408 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (213, 16%) | -17% (264, 9%) | 58% (1, 100%) | -100% (4, 0%) |
| wide_sl50_tp100 | -53% (213, 17%) | -17% (264, 9%) | 58% (1, 100%) | -100% (4, 0%) |
| sl30_tp50 | -55% (213, 20%) | -18% (264, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| sl50_tp50 | -55% (213, 22%) | -18% (264, 9%) | 24% (1, 100%) | -100% (4, 0%) |
| no_stop_tp100 | -54% (213, 18%) | -17% (264, 9%) | 58% (1, 100%) | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9076. Outcomes:

- missed_window: 6019
- low_liquidity: 2002
- proven_liquidity_gone: 329
- no_momentum: 312
- research_failed: 240
- simulated failed buy: 91
- proven_low_volume: 61
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 6
- proven: 5
- research_passed: 1
- dip: 1

Warning: 60 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
