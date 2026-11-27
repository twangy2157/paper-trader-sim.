# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T13:30:40Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 14. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3965 | 12% | -65.2% | -67 to -63 | -258751 |
| all momentum | 3989 | 12% | -64.9% | -67 to -63 | -259238 |
| control | 4766 | 6% | -19.3% | -20 to -18 | -92488 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 137 | 32% | -31.5% | -40 to -23 | -4326 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3968, 12%) | -19% (4766, 6%) | -13% (47, 28%) | -31% (137, 32%) |
| wide_sl50_tp100 | -65% (3968, 13%) | -20% (4766, 6%) | -13% (47, 32%) | -33% (137, 32%) |
| sl30_tp50 | -67% (3968, 14%) | -19% (4766, 7%) | -17% (47, 34%) | -32% (137, 33%) |
| sl50_tp50 | -67% (3968, 15%) | -20% (4766, 7%) | -18% (47, 38%) | -33% (137, 33%) |
| no_stop_tp100 | -65% (3968, 14%) | -20% (4766, 7%) | -12% (47, 32%) | -33% (137, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 127092. Outcomes:

- missed_window: 81758
- low_liquidity: 21956
- proven_liquidity_gone: 10889
- no_momentum: 4815
- research_failed: 3969
- simulated failed buy: 1625
- proven_low_volume: 1622
- proven_price_collapsed_or_parabolic: 171
- proven: 142
- proven_no_uptrend: 74
- dip: 47
- research_passed: 24

Warning: 1004 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
