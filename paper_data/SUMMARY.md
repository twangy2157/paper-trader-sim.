# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T05:29:13Z. Bankroll cash (research-selected trades): 564.24568815387. Open positions: 18. Pools on watchlist: 34.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3243 | 11% | -67.0% | -69 to -65 | -217647 |
| all momentum | 3263 | 11% | -66.7% | -69 to -65 | -218083 |
| control | 3969 | 6% | -19.2% | -20 to -18 | -76614 |
| dip buy | 43 | 26% | -13.5% | -30 to 3 | -583 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3242, 11%) | -19% (3969, 6%) | -14% (43, 26%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3242, 13%) | -19% (3969, 7%) | -13% (43, 30%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3242, 14%) | -19% (3969, 7%) | -16% (43, 33%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3242, 15%) | -20% (3969, 8%) | -17% (43, 37%) | -33% (123, 34%) |
| no_stop_tp100 | -66% (3242, 13%) | -20% (3969, 7%) | -12% (43, 30%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 107608. Outcomes:

- missed_window: 69860
- low_liquidity: 18047
- proven_liquidity_gone: 9295
- no_momentum: 4019
- research_failed: 3252
- proven_low_volume: 1381
- simulated failed buy: 1345
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 43
- research_passed: 20

Warning: 848 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
