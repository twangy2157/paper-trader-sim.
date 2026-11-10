# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T01:16:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 25. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1410 | 12% | -63.4% | -66 to -60 | -89497 |
| all momentum | 1426 | 12% | -63.0% | -66 to -60 | -90040 |
| control | 2072 | 5% | -17.9% | -19 to -16 | -37383 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1405, 13%) | -18% (2072, 5%) | -39% (13, 8%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1405, 14%) | -18% (2072, 5%) | -45% (13, 8%) | -26% (75, 37%) |
| sl30_tp50 | -64% (1405, 16%) | -18% (2072, 6%) | -41% (13, 8%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1405, 17%) | -18% (2072, 6%) | -48% (13, 8%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1405, 15%) | -19% (2072, 5%) | -43% (13, 8%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 53268. Outcomes:

- missed_window: 35527
- low_liquidity: 8520
- proven_liquidity_gone: 3948
- no_momentum: 2130
- research_failed: 1421
- proven_low_volume: 825
- simulated failed buy: 672
- proven_price_collapsed_or_parabolic: 89
- proven: 75
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 459 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
