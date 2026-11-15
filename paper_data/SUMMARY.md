# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T10:28:16Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 39.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2500 | 12% | -65.7% | -68 to -63 | -164519 |
| all momentum | 2516 | 12% | -65.5% | -68 to -63 | -165063 |
| control | 3200 | 6% | -18.7% | -20 to -17 | -60266 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 110 | 34% | -34.0% | -44 to -24 | -3748 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2495, 12%) | -19% (3200, 6%) | -12% (33, 30%) | -34% (110, 34%) |
| wide_sl50_tp100 | -66% (2495, 13%) | -19% (3200, 6%) | -15% (33, 33%) | -35% (110, 34%) |
| sl30_tp50 | -67% (2495, 14%) | -19% (3200, 7%) | -18% (33, 33%) | -34% (110, 35%) |
| sl50_tp50 | -67% (2495, 16%) | -19% (3200, 7%) | -21% (33, 36%) | -35% (110, 35%) |
| no_stop_tp100 | -66% (2495, 14%) | -19% (3200, 6%) | -13% (33, 33%) | -36% (110, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 87108. Outcomes:

- missed_window: 57229
- low_liquidity: 14294
- proven_liquidity_gone: 7257
- no_momentum: 3253
- research_failed: 2510
- proven_low_volume: 1151
- simulated failed buy: 1067
- proven_price_collapsed_or_parabolic: 135
- proven: 111
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 675 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
