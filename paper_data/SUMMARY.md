# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T09:51:43Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1478 | 12% | -63.6% | -67 to -61 | -94187 |
| all momentum | 1494 | 12% | -63.3% | -66 to -60 | -94730 |
| control | 2170 | 5% | -17.9% | -19 to -17 | -39068 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 76 | 37% | -25.8% | -37 to -14 | -1965 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1473, 13%) | -18% (2170, 5%) | -33% (15, 13%) | -26% (76, 37%) |
| wide_sl50_tp100 | -63% (1473, 14%) | -18% (2170, 5%) | -39% (15, 13%) | -27% (76, 37%) |
| sl30_tp50 | -65% (1473, 15%) | -18% (2170, 6%) | -37% (15, 13%) | -27% (76, 37%) |
| sl50_tp50 | -64% (1473, 17%) | -18% (2170, 6%) | -43% (15, 13%) | -28% (76, 37%) |
| no_stop_tp100 | -63% (1473, 15%) | -19% (2170, 5%) | -35% (15, 13%) | -27% (76, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 55424. Outcomes:

- missed_window: 36936
- low_liquidity: 8830
- proven_liquidity_gone: 4141
- no_momentum: 2222
- research_failed: 1486
- proven_low_volume: 872
- simulated failed buy: 697
- proven_price_collapsed_or_parabolic: 97
- proven: 77
- proven_no_uptrend: 35
- research_passed: 16
- dip: 15

Warning: 470 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
