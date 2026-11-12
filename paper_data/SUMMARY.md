# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T20:37:08Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1992 | 12% | -65.0% | -67 to -62 | -129643 |
| all momentum | 2008 | 12% | -64.7% | -67 to -62 | -130187 |
| control | 2763 | 6% | -17.8% | -19 to -16 | -49537 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 95 | 35% | -30.4% | -41 to -20 | -2892 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1987, 12%) | -18% (2763, 6%) | -20% (27, 26%) | -30% (95, 35%) |
| wide_sl50_tp100 | -65% (1987, 13%) | -18% (2763, 6%) | -23% (27, 30%) | -32% (95, 35%) |
| sl30_tp50 | -66% (1987, 15%) | -18% (2763, 6%) | -25% (27, 30%) | -30% (95, 36%) |
| sl50_tp50 | -66% (1987, 16%) | -18% (2763, 7%) | -28% (27, 33%) | -32% (95, 36%) |
| no_stop_tp100 | -65% (1987, 14%) | -18% (2763, 6%) | -21% (27, 30%) | -33% (95, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 70468. Outcomes:

- missed_window: 46430
- low_liquidity: 11369
- proven_liquidity_gone: 5615
- no_momentum: 2817
- research_failed: 2002
- proven_low_volume: 1048
- simulated failed buy: 883
- proven_price_collapsed_or_parabolic: 121
- proven: 97
- proven_no_uptrend: 42
- dip: 28
- research_passed: 16

Warning: 582 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
