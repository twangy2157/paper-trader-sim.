# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T04:20:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 12. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2438 | 12% | -65.5% | -68 to -63 | -160024 |
| all momentum | 2454 | 12% | -65.3% | -68 to -63 | -160567 |
| control | 3164 | 6% | -18.8% | -20 to -18 | -59657 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 110 | 34% | -34.0% | -44 to -24 | -3747 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2433, 12%) | -19% (3164, 6%) | -12% (33, 30%) | -34% (110, 34%) |
| wide_sl50_tp100 | -66% (2433, 13%) | -19% (3164, 6%) | -15% (33, 33%) | -35% (110, 34%) |
| sl30_tp50 | -67% (2433, 14%) | -19% (3164, 7%) | -18% (33, 33%) | -34% (110, 35%) |
| sl50_tp50 | -67% (2433, 16%) | -19% (3164, 7%) | -21% (33, 36%) | -35% (110, 35%) |
| no_stop_tp100 | -65% (2433, 14%) | -19% (3164, 6%) | -13% (33, 33%) | -36% (110, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 85581. Outcomes:

- missed_window: 56256
- low_liquidity: 14045
- proven_liquidity_gone: 7092
- no_momentum: 3212
- research_failed: 2446
- proven_low_volume: 1141
- simulated failed buy: 1043
- proven_price_collapsed_or_parabolic: 135
- proven: 110
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 664 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
