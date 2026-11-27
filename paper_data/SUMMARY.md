# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T22:25:36Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 28. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3972 | 12% | -65.2% | -67 to -63 | -259265 |
| all momentum | 3996 | 12% | -64.9% | -67 to -63 | -259752 |
| control | 4774 | 6% | -19.3% | -20 to -18 | -92630 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 142 | 31% | -31.9% | -41 to -23 | -4543 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3975, 12%) | -19% (4774, 6%) | -13% (47, 28%) | -32% (142, 31%) |
| wide_sl50_tp100 | -65% (3975, 13%) | -20% (4774, 6%) | -13% (47, 32%) | -33% (142, 31%) |
| sl30_tp50 | -67% (3975, 14%) | -19% (4774, 7%) | -17% (47, 34%) | -32% (142, 32%) |
| sl50_tp50 | -67% (3975, 15%) | -20% (4774, 7%) | -18% (47, 38%) | -33% (142, 32%) |
| no_stop_tp100 | -65% (3975, 14%) | -20% (4774, 7%) | -12% (47, 32%) | -33% (142, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 127434. Outcomes:

- missed_window: 81946
- low_liquidity: 22068
- proven_liquidity_gone: 10891
- no_momentum: 4832
- research_failed: 3985
- simulated failed buy: 1631
- proven_low_volume: 1622
- proven_price_collapsed_or_parabolic: 171
- proven: 142
- proven_no_uptrend: 74
- dip: 48
- research_passed: 24

Warning: 1007 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
