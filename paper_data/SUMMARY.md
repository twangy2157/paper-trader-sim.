# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T14:10:39Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2527 | 12% | -65.8% | -68 to -64 | -166424 |
| all momentum | 2543 | 12% | -65.6% | -68 to -63 | -166967 |
| control | 3238 | 6% | -18.7% | -20 to -17 | -60950 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 111 | 33% | -33.7% | -43 to -24 | -3752 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2522, 12%) | -19% (3238, 6%) | -12% (34, 29%) | -34% (111, 33%) |
| wide_sl50_tp100 | -66% (2522, 13%) | -19% (3238, 6%) | -15% (34, 32%) | -35% (111, 33%) |
| sl30_tp50 | -67% (2522, 14%) | -19% (3238, 7%) | -18% (34, 32%) | -34% (111, 34%) |
| sl50_tp50 | -67% (2522, 16%) | -19% (3238, 7%) | -21% (34, 35%) | -35% (111, 34%) |
| no_stop_tp100 | -66% (2522, 14%) | -19% (3238, 6%) | -13% (34, 32%) | -36% (111, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 87929. Outcomes:

- missed_window: 57707
- low_liquidity: 14443
- proven_liquidity_gone: 7349
- no_momentum: 3290
- research_failed: 2541
- proven_low_volume: 1162
- simulated failed buy: 1086
- proven_price_collapsed_or_parabolic: 136
- proven: 112
- proven_no_uptrend: 53
- dip: 34
- research_passed: 16

Warning: 686 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
