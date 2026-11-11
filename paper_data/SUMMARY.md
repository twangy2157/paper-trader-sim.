# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T00:24:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1639 | 12% | -64.9% | -68 to -62 | -106453 |
| all momentum | 1655 | 12% | -64.6% | -67 to -62 | -106996 |
| control | 2375 | 5% | -18.0% | -19 to -17 | -42961 |
| dip buy | 17 | 24% | -20.2% | -47 to 8 | -345 |
| proven pools | 79 | 37% | -26.1% | -37 to -15 | -2066 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1634, 12%) | -18% (2375, 5%) | -20% (17, 24%) | -26% (79, 37%) |
| wide_sl50_tp100 | -65% (1634, 13%) | -18% (2375, 5%) | -26% (17, 24%) | -27% (79, 37%) |
| sl30_tp50 | -66% (1634, 15%) | -18% (2375, 6%) | -29% (17, 24%) | -27% (79, 37%) |
| sl50_tp50 | -65% (1634, 16%) | -19% (2375, 6%) | -34% (17, 24%) | -28% (79, 37%) |
| no_stop_tp100 | -65% (1634, 14%) | -19% (2375, 5%) | -22% (17, 24%) | -27% (79, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 59546. Outcomes:

- missed_window: 39472
- low_liquidity: 9545
- proven_liquidity_gone: 4485
- no_momentum: 2431
- research_failed: 1649
- proven_low_volume: 948
- simulated failed buy: 765
- proven_price_collapsed_or_parabolic: 103
- proven: 79
- proven_no_uptrend: 36
- dip: 17
- research_passed: 16

Warning: 511 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
