# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T04:56:36Z. Bankroll cash (research-selected trades): 564.24568815387. Open positions: 19. Pools on watchlist: 34.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3241 | 11% | -67.0% | -69 to -65 | -217446 |
| all momentum | 3261 | 11% | -66.7% | -69 to -65 | -217882 |
| control | 3964 | 6% | -19.2% | -20 to -18 | -76491 |
| dip buy | 42 | 26% | -13.0% | -30 to 5 | -548 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3240, 11%) | -19% (3964, 6%) | -13% (42, 26%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3240, 13%) | -19% (3964, 7%) | -16% (42, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3240, 14%) | -19% (3964, 7%) | -17% (42, 31%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3240, 15%) | -20% (3964, 8%) | -18% (42, 36%) | -33% (123, 34%) |
| no_stop_tp100 | -66% (3240, 13%) | -20% (3964, 7%) | -15% (42, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 107496. Outcomes:

- missed_window: 69807
- low_liquidity: 18014
- proven_liquidity_gone: 9278
- no_momentum: 4016
- research_failed: 3248
- proven_low_volume: 1379
- simulated failed buy: 1345
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 43
- research_passed: 20

Warning: 848 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
