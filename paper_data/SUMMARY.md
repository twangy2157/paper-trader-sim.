# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T18:19:39Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 79.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1977 | 12% | -64.9% | -67 to -62 | -128394 |
| all momentum | 1993 | 12% | -64.6% | -67 to -62 | -128938 |
| control | 2747 | 6% | -17.9% | -19 to -17 | -49538 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 93 | 35% | -29.0% | -40 to -19 | -2708 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1972, 12%) | -18% (2747, 6%) | -20% (27, 26%) | -29% (93, 35%) |
| wide_sl50_tp100 | -65% (1972, 13%) | -18% (2747, 6%) | -23% (27, 30%) | -31% (93, 35%) |
| sl30_tp50 | -66% (1972, 15%) | -18% (2747, 6%) | -25% (27, 30%) | -30% (93, 35%) |
| sl50_tp50 | -66% (1972, 16%) | -18% (2747, 7%) | -28% (27, 33%) | -32% (93, 35%) |
| no_stop_tp100 | -65% (1972, 14%) | -18% (2747, 6%) | -21% (27, 30%) | -31% (93, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 69913. Outcomes:

- missed_window: 46082
- low_liquidity: 11277
- proven_liquidity_gone: 5552
- no_momentum: 2798
- research_failed: 1982
- proven_low_volume: 1045
- simulated failed buy: 876
- proven_price_collapsed_or_parabolic: 119
- proven: 97
- proven_no_uptrend: 42
- dip: 27
- research_passed: 16

Warning: 577 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
