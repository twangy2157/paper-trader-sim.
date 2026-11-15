# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T09:56:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 27. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2492 | 12% | -65.7% | -68 to -63 | -164008 |
| all momentum | 2508 | 12% | -65.5% | -68 to -63 | -164551 |
| control | 3192 | 6% | -18.8% | -20 to -18 | -60239 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 110 | 34% | -34.0% | -44 to -24 | -3748 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2487, 12%) | -19% (3192, 6%) | -12% (33, 30%) | -34% (110, 34%) |
| wide_sl50_tp100 | -66% (2487, 13%) | -19% (3192, 6%) | -15% (33, 33%) | -35% (110, 34%) |
| sl30_tp50 | -67% (2487, 14%) | -19% (3192, 7%) | -18% (33, 33%) | -34% (110, 35%) |
| sl50_tp50 | -67% (2487, 16%) | -19% (3192, 7%) | -21% (33, 36%) | -35% (110, 35%) |
| no_stop_tp100 | -66% (2487, 14%) | -19% (3192, 6%) | -13% (33, 33%) | -36% (110, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 86982. Outcomes:

- missed_window: 57144
- low_liquidity: 14281
- proven_liquidity_gone: 7239
- no_momentum: 3250
- research_failed: 2504
- proven_low_volume: 1151
- simulated failed buy: 1066
- proven_price_collapsed_or_parabolic: 135
- proven: 111
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 674 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
