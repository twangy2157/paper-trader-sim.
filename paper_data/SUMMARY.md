# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T22:36:00Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 23. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3974 | 12% | -65.1% | -67 to -63 | -259179 |
| all momentum | 3998 | 12% | -64.9% | -67 to -63 | -259666 |
| control | 4779 | 6% | -19.3% | -20 to -18 | -92660 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 142 | 31% | -31.9% | -41 to -23 | -4543 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3977, 12%) | -19% (4779, 6%) | -13% (47, 28%) | -32% (142, 31%) |
| wide_sl50_tp100 | -65% (3977, 13%) | -20% (4779, 6%) | -13% (47, 32%) | -33% (142, 31%) |
| sl30_tp50 | -67% (3977, 14%) | -19% (4779, 7%) | -17% (47, 34%) | -32% (142, 32%) |
| sl50_tp50 | -67% (3977, 15%) | -20% (4779, 7%) | -18% (47, 38%) | -33% (142, 32%) |
| no_stop_tp100 | -65% (3977, 14%) | -20% (4779, 7%) | -12% (47, 32%) | -33% (142, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 127475. Outcomes:

- missed_window: 81977
- low_liquidity: 22076
- proven_liquidity_gone: 10891
- no_momentum: 4834
- research_failed: 3985
- simulated failed buy: 1631
- proven_low_volume: 1622
- proven_price_collapsed_or_parabolic: 171
- proven: 142
- proven_no_uptrend: 74
- dip: 48
- research_passed: 24

Warning: 1007 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
