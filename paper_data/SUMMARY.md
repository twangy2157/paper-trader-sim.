# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T19:22:33Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 67.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1982 | 12% | -64.9% | -67 to -62 | -128896 |
| all momentum | 1998 | 12% | -64.7% | -67 to -62 | -129439 |
| control | 2754 | 6% | -17.9% | -19 to -17 | -49478 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 95 | 35% | -30.4% | -41 to -20 | -2892 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1977, 12%) | -18% (2754, 6%) | -20% (27, 26%) | -30% (95, 35%) |
| wide_sl50_tp100 | -65% (1977, 13%) | -18% (2754, 6%) | -23% (27, 30%) | -32% (95, 35%) |
| sl30_tp50 | -66% (1977, 15%) | -18% (2754, 6%) | -25% (27, 30%) | -30% (95, 36%) |
| sl50_tp50 | -66% (1977, 16%) | -18% (2754, 7%) | -28% (27, 33%) | -32% (95, 36%) |
| no_stop_tp100 | -65% (1977, 14%) | -18% (2754, 6%) | -21% (27, 30%) | -33% (95, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 70180. Outcomes:

- missed_window: 46261
- low_liquidity: 11320
- proven_liquidity_gone: 5576
- no_momentum: 2804
- research_failed: 1990
- proven_low_volume: 1048
- simulated failed buy: 878
- proven_price_collapsed_or_parabolic: 121
- proven: 97
- proven_no_uptrend: 42
- dip: 27
- research_passed: 16

Warning: 579 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
