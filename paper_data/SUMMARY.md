# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T06:33:14Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1456 | 12% | -63.7% | -67 to -61 | -92853 |
| all momentum | 1472 | 12% | -63.4% | -66 to -60 | -93397 |
| control | 2138 | 5% | -17.9% | -19 to -16 | -38474 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1451, 12%) | -18% (2138, 5%) | -33% (15, 13%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1451, 14%) | -18% (2138, 5%) | -39% (15, 13%) | -26% (75, 37%) |
| sl30_tp50 | -65% (1451, 15%) | -18% (2138, 6%) | -37% (15, 13%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1451, 17%) | -18% (2138, 6%) | -43% (15, 13%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1451, 15%) | -19% (2138, 5%) | -35% (15, 13%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 54703. Outcomes:

- missed_window: 36478
- low_liquidity: 8720
- proven_liquidity_gone: 4070
- no_momentum: 2196
- research_failed: 1460
- proven_low_volume: 856
- simulated failed buy: 687
- proven_price_collapsed_or_parabolic: 96
- proven: 76
- proven_no_uptrend: 33
- research_passed: 16
- dip: 15

Warning: 466 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
