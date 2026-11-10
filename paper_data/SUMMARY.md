# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T08:36:12Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 30. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1461 | 12% | -63.7% | -67 to -61 | -93237 |
| all momentum | 1477 | 12% | -63.4% | -66 to -60 | -93781 |
| control | 2155 | 5% | -17.9% | -19 to -16 | -38784 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 76 | 37% | -25.8% | -37 to -14 | -1965 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1456, 12%) | -18% (2155, 5%) | -33% (15, 13%) | -26% (76, 37%) |
| wide_sl50_tp100 | -63% (1456, 14%) | -18% (2155, 5%) | -39% (15, 13%) | -27% (76, 37%) |
| sl30_tp50 | -65% (1456, 15%) | -18% (2155, 6%) | -37% (15, 13%) | -27% (76, 37%) |
| sl50_tp50 | -64% (1456, 17%) | -18% (2155, 6%) | -43% (15, 13%) | -28% (76, 37%) |
| no_stop_tp100 | -63% (1456, 15%) | -19% (2155, 5%) | -35% (15, 13%) | -27% (76, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 55097. Outcomes:

- missed_window: 36710
- low_liquidity: 8784
- proven_liquidity_gone: 4117
- no_momentum: 2214
- research_failed: 1475
- proven_low_volume: 865
- simulated failed buy: 692
- proven_price_collapsed_or_parabolic: 97
- proven: 77
- proven_no_uptrend: 35
- research_passed: 16
- dip: 15

Warning: 468 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
