# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T07:08:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 4. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2472 | 12% | -65.7% | -68 to -63 | -162640 |
| all momentum | 2488 | 12% | -65.5% | -68 to -63 | -163184 |
| control | 3178 | 6% | -18.8% | -20 to -18 | -59958 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 110 | 34% | -34.0% | -44 to -24 | -3747 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2467, 12%) | -19% (3178, 6%) | -12% (33, 30%) | -34% (110, 34%) |
| wide_sl50_tp100 | -66% (2467, 13%) | -19% (3178, 6%) | -15% (33, 33%) | -35% (110, 34%) |
| sl30_tp50 | -67% (2467, 14%) | -19% (3178, 7%) | -18% (33, 33%) | -34% (110, 35%) |
| sl50_tp50 | -67% (2467, 16%) | -19% (3178, 7%) | -21% (33, 36%) | -35% (110, 35%) |
| no_stop_tp100 | -66% (2467, 14%) | -19% (3178, 6%) | -13% (33, 33%) | -36% (110, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 86217. Outcomes:

- missed_window: 56673
- low_liquidity: 14142
- proven_liquidity_gone: 7157
- no_momentum: 3224
- research_failed: 2474
- proven_low_volume: 1148
- simulated failed buy: 1053
- proven_price_collapsed_or_parabolic: 135
- proven: 110
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 670 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
