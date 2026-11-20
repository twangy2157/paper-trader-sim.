# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T02:28:44Z. Bankroll cash (research-selected trades): 564.24568815387. Open positions: 16. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3219 | 11% | -67.1% | -69 to -65 | -216224 |
| all momentum | 3239 | 11% | -66.8% | -69 to -65 | -216659 |
| control | 3944 | 6% | -19.1% | -20 to -18 | -75878 |
| dip buy | 42 | 26% | -13.0% | -30 to 5 | -548 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3218, 11%) | -19% (3944, 6%) | -13% (42, 26%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3218, 13%) | -19% (3944, 7%) | -16% (42, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3218, 14%) | -19% (3944, 7%) | -17% (42, 31%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3218, 15%) | -20% (3944, 8%) | -18% (42, 36%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3218, 13%) | -20% (3944, 7%) | -15% (42, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 106796. Outcomes:

- missed_window: 69361
- low_liquidity: 17888
- proven_liquidity_gone: 9210
- no_momentum: 3997
- research_failed: 3226
- proven_low_volume: 1375
- simulated failed buy: 1334
- proven_price_collapsed_or_parabolic: 158
- proven: 123
- proven_no_uptrend: 62
- dip: 42
- research_passed: 20

Warning: 841 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
