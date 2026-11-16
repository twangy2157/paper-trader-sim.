# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-16T09:31:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2656 | 12% | -66.0% | -68 to -64 | -175482 |
| all momentum | 2672 | 12% | -65.8% | -68 to -63 | -176026 |
| control | 3390 | 6% | -18.9% | -20 to -18 | -64248 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2651, 12%) | -19% (3390, 6%) | -13% (35, 29%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2651, 13%) | -19% (3390, 6%) | -15% (35, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2651, 14%) | -19% (3390, 7%) | -18% (35, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2651, 15%) | -19% (3390, 7%) | -19% (35, 37%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2651, 14%) | -19% (3390, 6%) | -13% (35, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 92207. Outcomes:

- missed_window: 60488
- low_liquidity: 15113
- proven_liquidity_gone: 7772
- no_momentum: 3444
- research_failed: 2667
- proven_low_volume: 1221
- simulated failed buy: 1135
- proven_price_collapsed_or_parabolic: 144
- proven: 114
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 726 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
