# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T20:26:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 26. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1990 | 12% | -65.0% | -68 to -62 | -129536 |
| all momentum | 2006 | 12% | -64.8% | -67 to -62 | -130079 |
| control | 2760 | 6% | -17.9% | -19 to -17 | -49573 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 95 | 35% | -30.4% | -41 to -20 | -2892 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1985, 12%) | -18% (2760, 6%) | -20% (27, 26%) | -30% (95, 35%) |
| wide_sl50_tp100 | -65% (1985, 13%) | -18% (2760, 6%) | -23% (27, 30%) | -32% (95, 35%) |
| sl30_tp50 | -66% (1985, 15%) | -18% (2760, 6%) | -25% (27, 30%) | -30% (95, 36%) |
| sl50_tp50 | -66% (1985, 16%) | -18% (2760, 7%) | -28% (27, 33%) | -32% (95, 36%) |
| no_stop_tp100 | -65% (1985, 14%) | -18% (2760, 6%) | -21% (27, 30%) | -33% (95, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 70432. Outcomes:

- missed_window: 46407
- low_liquidity: 11364
- proven_liquidity_gone: 5609
- no_momentum: 2816
- research_failed: 2001
- proven_low_volume: 1048
- simulated failed buy: 883
- proven_price_collapsed_or_parabolic: 121
- proven: 97
- proven_no_uptrend: 42
- dip: 28
- research_passed: 16

Warning: 582 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
