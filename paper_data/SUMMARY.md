# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T17:31:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2559 | 12% | -65.9% | -68 to -64 | -168805 |
| all momentum | 2575 | 12% | -65.7% | -68 to -63 | -169348 |
| control | 3282 | 6% | -18.7% | -20 to -17 | -61730 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 112 | 34% | -33.2% | -43 to -23 | -3725 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2554, 12%) | -19% (3282, 6%) | -12% (34, 29%) | -33% (112, 34%) |
| wide_sl50_tp100 | -66% (2554, 13%) | -19% (3282, 6%) | -15% (34, 32%) | -34% (112, 34%) |
| sl30_tp50 | -67% (2554, 14%) | -19% (3282, 7%) | -18% (34, 32%) | -33% (112, 35%) |
| sl50_tp50 | -67% (2554, 16%) | -19% (3282, 7%) | -21% (34, 35%) | -34% (112, 35%) |
| no_stop_tp100 | -66% (2554, 14%) | -19% (3282, 6%) | -13% (34, 32%) | -35% (112, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 88931. Outcomes:

- missed_window: 58395
- low_liquidity: 14574
- proven_liquidity_gone: 7427
- no_momentum: 3337
- research_failed: 2566
- proven_low_volume: 1176
- simulated failed buy: 1101
- proven_price_collapsed_or_parabolic: 137
- proven: 112
- proven_no_uptrend: 56
- dip: 34
- research_passed: 16

Warning: 700 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
