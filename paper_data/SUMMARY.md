# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T08:13:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1886 | 12% | -64.6% | -67 to -62 | -122060 |
| all momentum | 1902 | 12% | -64.4% | -67 to -62 | -122604 |
| control | 2658 | 6% | -18.0% | -19 to -17 | -47978 |
| dip buy | 25 | 24% | -20.0% | -43 to 4 | -502 |
| proven pools | 89 | 35% | -28.6% | -39 to -18 | -2554 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1881, 12%) | -18% (2658, 6%) | -20% (25, 24%) | -29% (89, 35%) |
| wide_sl50_tp100 | -65% (1881, 13%) | -18% (2658, 6%) | -23% (25, 28%) | -30% (89, 35%) |
| sl30_tp50 | -66% (1881, 15%) | -18% (2658, 6%) | -29% (25, 24%) | -30% (89, 35%) |
| sl50_tp50 | -66% (1881, 16%) | -18% (2658, 7%) | -32% (25, 28%) | -31% (89, 35%) |
| no_stop_tp100 | -65% (1881, 14%) | -18% (2658, 6%) | -21% (25, 28%) | -31% (89, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 67452. Outcomes:

- missed_window: 44562
- low_liquidity: 10839
- proven_liquidity_gone: 5289
- no_momentum: 2709
- research_failed: 1895
- proven_low_volume: 1025
- simulated failed buy: 844
- proven_price_collapsed_or_parabolic: 117
- proven: 91
- proven_no_uptrend: 39
- dip: 26
- research_passed: 16

Warning: 558 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
