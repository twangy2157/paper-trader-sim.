# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T07:21:15Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 6. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1459 | 12% | -63.8% | -67 to -61 | -93153 |
| all momentum | 1475 | 12% | -63.4% | -67 to -60 | -93697 |
| control | 2149 | 5% | -17.9% | -19 to -16 | -38644 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 76 | 37% | -25.8% | -37 to -14 | -1965 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1454, 12%) | -18% (2149, 5%) | -33% (15, 13%) | -26% (76, 37%) |
| wide_sl50_tp100 | -63% (1454, 14%) | -18% (2149, 5%) | -39% (15, 13%) | -27% (76, 37%) |
| sl30_tp50 | -65% (1454, 15%) | -18% (2149, 6%) | -37% (15, 13%) | -27% (76, 37%) |
| sl50_tp50 | -64% (1454, 17%) | -18% (2149, 6%) | -43% (15, 13%) | -28% (76, 37%) |
| no_stop_tp100 | -63% (1454, 15%) | -18% (2149, 5%) | -35% (15, 13%) | -27% (76, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 54805. Outcomes:

- missed_window: 36554
- low_liquidity: 8729
- proven_liquidity_gone: 4081
- no_momentum: 2197
- research_failed: 1461
- proven_low_volume: 859
- simulated failed buy: 687
- proven_price_collapsed_or_parabolic: 97
- proven: 76
- proven_no_uptrend: 33
- research_passed: 16
- dip: 15

Warning: 466 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
