# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T10:38:32Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 31.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2502 | 12% | -65.7% | -68 to -63 | -164719 |
| all momentum | 2518 | 12% | -65.5% | -68 to -63 | -165263 |
| control | 3202 | 6% | -18.7% | -20 to -18 | -60283 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 110 | 34% | -34.0% | -44 to -24 | -3748 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2497, 12%) | -19% (3202, 6%) | -12% (33, 30%) | -34% (110, 34%) |
| wide_sl50_tp100 | -66% (2497, 13%) | -19% (3202, 6%) | -15% (33, 33%) | -35% (110, 34%) |
| sl30_tp50 | -67% (2497, 14%) | -19% (3202, 7%) | -18% (33, 33%) | -34% (110, 35%) |
| sl50_tp50 | -67% (2497, 16%) | -19% (3202, 7%) | -21% (33, 36%) | -35% (110, 35%) |
| no_stop_tp100 | -66% (2497, 14%) | -19% (3202, 6%) | -13% (33, 33%) | -36% (110, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 87147. Outcomes:

- missed_window: 57251
- low_liquidity: 14303
- proven_liquidity_gone: 7262
- no_momentum: 3255
- research_failed: 2510
- proven_low_volume: 1152
- simulated failed buy: 1067
- proven_price_collapsed_or_parabolic: 135
- proven: 111
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 675 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
