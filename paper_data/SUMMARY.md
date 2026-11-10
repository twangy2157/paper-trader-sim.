# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T12:22:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1499 | 12% | -63.6% | -66 to -61 | -95454 |
| all momentum | 1515 | 12% | -63.3% | -66 to -60 | -95998 |
| control | 2192 | 5% | -18.0% | -19 to -17 | -39640 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 77 | 36% | -26.7% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1494, 13%) | -18% (2192, 5%) | -33% (15, 13%) | -27% (77, 36%) |
| wide_sl50_tp100 | -63% (1494, 14%) | -18% (2192, 5%) | -39% (15, 13%) | -27% (77, 36%) |
| sl30_tp50 | -65% (1494, 15%) | -18% (2192, 6%) | -37% (15, 13%) | -28% (77, 36%) |
| sl50_tp50 | -64% (1494, 17%) | -18% (2192, 6%) | -43% (15, 13%) | -29% (77, 36%) |
| no_stop_tp100 | -63% (1494, 15%) | -19% (2192, 5%) | -35% (15, 13%) | -28% (77, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 56087. Outcomes:

- missed_window: 37360
- low_liquidity: 8934
- proven_liquidity_gone: 4214
- no_momentum: 2251
- research_failed: 1507
- proven_low_volume: 875
- simulated failed buy: 704
- proven_price_collapsed_or_parabolic: 98
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 15

Warning: 473 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
