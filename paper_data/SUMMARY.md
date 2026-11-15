# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T12:13:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2518 | 12% | -65.8% | -68 to -64 | -165815 |
| all momentum | 2534 | 12% | -65.6% | -68 to -63 | -166359 |
| control | 3216 | 6% | -18.7% | -20 to -17 | -60548 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 111 | 33% | -33.7% | -43 to -24 | -3752 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2513, 12%) | -19% (3216, 6%) | -12% (33, 30%) | -34% (111, 33%) |
| wide_sl50_tp100 | -66% (2513, 13%) | -19% (3216, 6%) | -15% (33, 33%) | -35% (111, 33%) |
| sl30_tp50 | -67% (2513, 14%) | -19% (3216, 7%) | -18% (33, 33%) | -34% (111, 34%) |
| sl50_tp50 | -67% (2513, 16%) | -19% (3216, 7%) | -21% (33, 36%) | -35% (111, 34%) |
| no_stop_tp100 | -66% (2513, 14%) | -19% (3216, 6%) | -13% (33, 33%) | -36% (111, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 87487. Outcomes:

- missed_window: 57439
- low_liquidity: 14373
- proven_liquidity_gone: 7301
- no_momentum: 3274
- research_failed: 2523
- proven_low_volume: 1155
- simulated failed buy: 1074
- proven_price_collapsed_or_parabolic: 135
- proven: 112
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 680 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
