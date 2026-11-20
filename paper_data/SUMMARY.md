# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T06:00:36Z. Bankroll cash (research-selected trades): 564.24568815387. Open positions: 14. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3248 | 11% | -67.0% | -69 to -65 | -217764 |
| all momentum | 3268 | 11% | -66.7% | -69 to -65 | -218200 |
| control | 3973 | 6% | -19.2% | -20 to -18 | -76720 |
| dip buy | 43 | 26% | -13.5% | -30 to 3 | -583 |
| proven pools | 124 | 33% | -31.2% | -41 to -22 | -3884 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3247, 12%) | -19% (3973, 6%) | -14% (43, 26%) | -31% (124, 33%) |
| wide_sl50_tp100 | -67% (3247, 13%) | -19% (3973, 7%) | -13% (43, 30%) | -32% (124, 33%) |
| sl30_tp50 | -68% (3247, 14%) | -19% (3973, 7%) | -16% (43, 33%) | -32% (124, 34%) |
| sl50_tp50 | -68% (3247, 15%) | -20% (3973, 8%) | -17% (43, 37%) | -32% (124, 34%) |
| no_stop_tp100 | -66% (3247, 13%) | -20% (3973, 7%) | -12% (43, 30%) | -33% (124, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 107711. Outcomes:

- missed_window: 69912
- low_liquidity: 18069
- proven_liquidity_gone: 9314
- no_momentum: 4023
- research_failed: 3254
- proven_low_volume: 1381
- simulated failed buy: 1349
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 43
- research_passed: 20

Warning: 849 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
