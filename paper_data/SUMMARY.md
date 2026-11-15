# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T14:31:49Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2532 | 12% | -65.8% | -68 to -63 | -166739 |
| all momentum | 2548 | 12% | -65.6% | -68 to -63 | -167282 |
| control | 3239 | 6% | -18.7% | -20 to -18 | -60959 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 112 | 34% | -33.2% | -43 to -23 | -3725 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2527, 12%) | -19% (3239, 6%) | -12% (34, 29%) | -33% (112, 34%) |
| wide_sl50_tp100 | -66% (2527, 13%) | -19% (3239, 6%) | -15% (34, 32%) | -34% (112, 34%) |
| sl30_tp50 | -67% (2527, 14%) | -19% (3239, 7%) | -18% (34, 32%) | -33% (112, 35%) |
| sl50_tp50 | -67% (2527, 16%) | -19% (3239, 7%) | -21% (34, 35%) | -34% (112, 35%) |
| no_stop_tp100 | -66% (2527, 14%) | -19% (3239, 6%) | -13% (34, 32%) | -35% (112, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 88043. Outcomes:

- missed_window: 57784
- low_liquidity: 14463
- proven_liquidity_gone: 7359
- no_momentum: 3293
- research_failed: 2542
- proven_low_volume: 1164
- simulated failed buy: 1087
- proven_price_collapsed_or_parabolic: 136
- proven: 112
- proven_no_uptrend: 53
- dip: 34
- research_passed: 16

Warning: 687 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
