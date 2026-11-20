# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T03:41:53Z. Bankroll cash (research-selected trades): 564.24568815387. Open positions: 19. Pools on watchlist: 83.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3228 | 11% | -67.0% | -69 to -65 | -216678 |
| all momentum | 3248 | 11% | -66.8% | -69 to -65 | -217114 |
| control | 3955 | 6% | -19.2% | -20 to -18 | -76241 |
| dip buy | 42 | 26% | -13.0% | -30 to 5 | -548 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3227, 11%) | -19% (3955, 6%) | -13% (42, 26%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3227, 13%) | -19% (3955, 7%) | -16% (42, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3227, 14%) | -19% (3955, 7%) | -17% (42, 31%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3227, 15%) | -20% (3955, 8%) | -18% (42, 36%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3227, 13%) | -20% (3955, 7%) | -15% (42, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 107127. Outcomes:

- missed_window: 69564
- low_liquidity: 17948
- proven_liquidity_gone: 9248
- no_momentum: 4005
- research_failed: 3238
- proven_low_volume: 1377
- simulated failed buy: 1339
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 42
- research_passed: 20

Warning: 845 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
