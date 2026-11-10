# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T11:29:43Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1490 | 12% | -63.5% | -66 to -60 | -94706 |
| all momentum | 1506 | 13% | -63.2% | -66 to -60 | -95250 |
| control | 2183 | 5% | -18.1% | -20 to -17 | -39636 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 77 | 36% | -26.7% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1485, 13%) | -18% (2183, 5%) | -33% (15, 13%) | -27% (77, 36%) |
| wide_sl50_tp100 | -63% (1485, 14%) | -18% (2183, 5%) | -39% (15, 13%) | -27% (77, 36%) |
| sl30_tp50 | -64% (1485, 15%) | -18% (2183, 6%) | -37% (15, 13%) | -28% (77, 36%) |
| sl50_tp50 | -64% (1485, 17%) | -19% (2183, 6%) | -43% (15, 13%) | -29% (77, 36%) |
| no_stop_tp100 | -63% (1485, 15%) | -19% (2183, 5%) | -35% (15, 13%) | -28% (77, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 55861. Outcomes:

- missed_window: 37221
- low_liquidity: 8901
- proven_liquidity_gone: 4186
- no_momentum: 2237
- research_failed: 1502
- proven_low_volume: 873
- simulated failed buy: 700
- proven_price_collapsed_or_parabolic: 97
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 15

Warning: 472 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
