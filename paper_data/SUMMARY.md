# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T04:35:40Z. Bankroll cash (research-selected trades): 564.24568815387. Open positions: 21. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3237 | 11% | -67.0% | -69 to -65 | -217308 |
| all momentum | 3257 | 11% | -66.8% | -69 to -65 | -217743 |
| control | 3961 | 6% | -19.2% | -20 to -18 | -76473 |
| dip buy | 42 | 26% | -13.0% | -30 to 5 | -548 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3236, 11%) | -19% (3961, 6%) | -13% (42, 26%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3236, 13%) | -19% (3961, 7%) | -16% (42, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3236, 14%) | -19% (3961, 7%) | -17% (42, 31%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3236, 15%) | -20% (3961, 8%) | -18% (42, 36%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3236, 13%) | -20% (3961, 7%) | -15% (42, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 107401. Outcomes:

- missed_window: 69746
- low_liquidity: 18000
- proven_liquidity_gone: 9266
- no_momentum: 4014
- research_failed: 3245
- proven_low_volume: 1378
- simulated failed buy: 1343
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 43
- research_passed: 20

Warning: 847 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
