# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T23:39:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2599 | 12% | -66.0% | -68 to -64 | -171733 |
| all momentum | 2615 | 12% | -65.8% | -68 to -64 | -172277 |
| control | 3334 | 6% | -18.6% | -20 to -17 | -62390 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 113 | 34% | -33.8% | -43 to -24 | -3825 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2594, 12%) | -19% (3334, 6%) | -13% (35, 29%) | -34% (113, 34%) |
| wide_sl50_tp100 | -66% (2594, 13%) | -19% (3334, 6%) | -15% (35, 31%) | -35% (113, 34%) |
| sl30_tp50 | -67% (2594, 14%) | -19% (3334, 7%) | -18% (35, 31%) | -34% (113, 35%) |
| sl50_tp50 | -67% (2594, 15%) | -19% (3334, 7%) | -19% (35, 37%) | -35% (113, 35%) |
| no_stop_tp100 | -66% (2594, 14%) | -19% (3334, 6%) | -13% (35, 31%) | -36% (113, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 90433. Outcomes:

- missed_window: 59305
- low_liquidity: 14878
- proven_liquidity_gone: 7575
- no_momentum: 3385
- research_failed: 2609
- proven_low_volume: 1204
- simulated failed buy: 1117
- proven_price_collapsed_or_parabolic: 138
- proven: 113
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 713 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
