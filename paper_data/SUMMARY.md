# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-27T21:10:34Z. Bankroll cash (research-selected trades): 513.2029228559132. Open positions: 7. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 24 | 33% | -20.1% | -46 to 6 | -487 |
| momentum, not picked | 3968 | 12% | -65.2% | -67 to -63 | -259052 |
| all momentum | 3992 | 12% | -64.9% | -67 to -63 | -259539 |
| control | 4767 | 6% | -19.3% | -20 to -18 | -92496 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 141 | 31% | -32.1% | -41 to -24 | -4540 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3971, 12%) | -19% (4767, 6%) | -13% (47, 28%) | -32% (141, 31%) |
| wide_sl50_tp100 | -65% (3971, 13%) | -20% (4767, 6%) | -13% (47, 32%) | -33% (141, 31%) |
| sl30_tp50 | -67% (3971, 14%) | -19% (4767, 7%) | -17% (47, 34%) | -32% (141, 32%) |
| sl50_tp50 | -67% (3971, 15%) | -20% (4767, 7%) | -18% (47, 38%) | -33% (141, 32%) |
| no_stop_tp100 | -65% (3971, 14%) | -20% (4767, 7%) | -12% (47, 32%) | -34% (141, 31%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 127158. Outcomes:

- missed_window: 81809
- low_liquidity: 21966
- proven_liquidity_gone: 10891
- no_momentum: 4816
- research_failed: 3969
- simulated failed buy: 1627
- proven_low_volume: 1622
- proven_price_collapsed_or_parabolic: 171
- proven: 142
- proven_no_uptrend: 74
- dip: 47
- research_passed: 24

Warning: 1004 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
