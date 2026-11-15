# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T10:59:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2504 | 12% | -65.7% | -68 to -63 | -164854 |
| all momentum | 2520 | 12% | -65.5% | -68 to -63 | -165397 |
| control | 3206 | 6% | -18.7% | -20 to -17 | -60305 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 111 | 33% | -33.7% | -43 to -24 | -3752 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2499, 12%) | -19% (3206, 6%) | -12% (33, 30%) | -34% (111, 33%) |
| wide_sl50_tp100 | -66% (2499, 13%) | -19% (3206, 6%) | -15% (33, 33%) | -35% (111, 33%) |
| sl30_tp50 | -67% (2499, 14%) | -19% (3206, 7%) | -18% (33, 33%) | -34% (111, 34%) |
| sl50_tp50 | -67% (2499, 16%) | -19% (3206, 7%) | -21% (33, 36%) | -35% (111, 34%) |
| no_stop_tp100 | -66% (2499, 14%) | -19% (3206, 6%) | -13% (33, 33%) | -36% (111, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 87212. Outcomes:

- missed_window: 57286
- low_liquidity: 14319
- proven_liquidity_gone: 7265
- no_momentum: 3258
- research_failed: 2516
- proven_low_volume: 1152
- simulated failed buy: 1069
- proven_price_collapsed_or_parabolic: 135
- proven: 111
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 675 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
