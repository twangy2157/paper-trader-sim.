# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T17:48:27Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1974 | 12% | -64.9% | -67 to -62 | -128208 |
| all momentum | 1990 | 12% | -64.6% | -67 to -62 | -128752 |
| control | 2738 | 6% | -18.0% | -19 to -17 | -49664 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 93 | 35% | -29.0% | -40 to -19 | -2708 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1969, 12%) | -18% (2738, 6%) | -20% (27, 26%) | -29% (93, 35%) |
| wide_sl50_tp100 | -65% (1969, 13%) | -18% (2738, 6%) | -23% (27, 30%) | -31% (93, 35%) |
| sl30_tp50 | -66% (1969, 15%) | -18% (2738, 6%) | -25% (27, 30%) | -30% (93, 35%) |
| sl50_tp50 | -66% (1969, 16%) | -19% (2738, 7%) | -28% (27, 33%) | -32% (93, 35%) |
| no_stop_tp100 | -65% (1969, 14%) | -18% (2738, 6%) | -21% (27, 30%) | -31% (93, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 69770. Outcomes:

- missed_window: 45991
- low_liquidity: 11250
- proven_liquidity_gone: 5538
- no_momentum: 2796
- research_failed: 1979
- proven_low_volume: 1045
- simulated failed buy: 873
- proven_price_collapsed_or_parabolic: 119
- proven: 95
- proven_no_uptrend: 41
- dip: 27
- research_passed: 16

Warning: 576 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
