# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T19:35:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 11. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2574 | 12% | -65.9% | -68 to -64 | -169959 |
| all momentum | 2590 | 12% | -65.7% | -68 to -63 | -170503 |
| control | 3303 | 6% | -18.7% | -20 to -17 | -61987 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 112 | 34% | -33.2% | -43 to -23 | -3725 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2569, 12%) | -19% (3303, 6%) | -12% (34, 29%) | -33% (112, 34%) |
| wide_sl50_tp100 | -66% (2569, 13%) | -19% (3303, 6%) | -15% (34, 32%) | -34% (112, 34%) |
| sl30_tp50 | -67% (2569, 14%) | -19% (3303, 7%) | -18% (34, 32%) | -33% (112, 35%) |
| sl50_tp50 | -67% (2569, 15%) | -19% (3303, 7%) | -21% (34, 35%) | -34% (112, 35%) |
| no_stop_tp100 | -66% (2569, 14%) | -19% (3303, 6%) | -13% (34, 32%) | -35% (112, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 89385. Outcomes:

- missed_window: 58676
- low_liquidity: 14651
- proven_liquidity_gone: 7472
- no_momentum: 3352
- research_failed: 2579
- proven_low_volume: 1190
- simulated failed buy: 1108
- proven_price_collapsed_or_parabolic: 138
- proven: 113
- proven_no_uptrend: 56
- dip: 34
- research_passed: 16

Warning: 707 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
