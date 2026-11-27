# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T22:14:58Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 29. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3970 | 12% | -65.2% | -67 to -63 | -259158 |
| all momentum | 3994 | 12% | -64.9% | -67 to -63 | -259645 |
| control | 4772 | 6% | -19.3% | -20 to -18 | -92626 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 142 | 31% | -31.9% | -41 to -23 | -4543 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3973, 12%) | -19% (4772, 6%) | -13% (47, 28%) | -32% (142, 31%) |
| wide_sl50_tp100 | -65% (3973, 13%) | -20% (4772, 6%) | -13% (47, 32%) | -33% (142, 31%) |
| sl30_tp50 | -67% (3973, 14%) | -19% (4772, 7%) | -17% (47, 34%) | -32% (142, 32%) |
| sl50_tp50 | -67% (3973, 15%) | -20% (4772, 7%) | -18% (47, 38%) | -33% (142, 32%) |
| no_stop_tp100 | -65% (3973, 14%) | -20% (4772, 7%) | -12% (47, 32%) | -33% (142, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 127404. Outcomes:

- missed_window: 81931
- low_liquidity: 22056
- proven_liquidity_gone: 10891
- no_momentum: 4832
- research_failed: 3982
- simulated failed buy: 1631
- proven_low_volume: 1622
- proven_price_collapsed_or_parabolic: 171
- proven: 142
- proven_no_uptrend: 74
- dip: 48
- research_passed: 24

Warning: 1006 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
