# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T13:48:56Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 26. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2525 | 12% | -65.7% | -68 to -64 | -166223 |
| all momentum | 2541 | 12% | -65.5% | -68 to -63 | -166767 |
| control | 3233 | 6% | -18.8% | -20 to -18 | -60916 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 111 | 33% | -33.7% | -43 to -24 | -3752 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2520, 12%) | -19% (3233, 6%) | -12% (33, 30%) | -34% (111, 33%) |
| wide_sl50_tp100 | -66% (2520, 13%) | -19% (3233, 6%) | -15% (33, 33%) | -35% (111, 33%) |
| sl30_tp50 | -67% (2520, 14%) | -19% (3233, 7%) | -18% (33, 33%) | -34% (111, 34%) |
| sl50_tp50 | -67% (2520, 16%) | -19% (3233, 7%) | -21% (33, 36%) | -35% (111, 34%) |
| no_stop_tp100 | -66% (2520, 14%) | -19% (3233, 6%) | -13% (33, 33%) | -36% (111, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 87837. Outcomes:

- missed_window: 57644
- low_liquidity: 14432
- proven_liquidity_gone: 7339
- no_momentum: 3288
- research_failed: 2538
- proven_low_volume: 1161
- simulated failed buy: 1084
- proven_price_collapsed_or_parabolic: 136
- proven: 112
- proven_no_uptrend: 53
- dip: 34
- research_passed: 16

Warning: 684 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
