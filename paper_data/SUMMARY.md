# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T01:05:14Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 32. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1405 | 12% | -63.6% | -67 to -60 | -89437 |
| all momentum | 1421 | 12% | -63.2% | -66 to -60 | -89981 |
| control | 2069 | 5% | -18.0% | -20 to -17 | -37366 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1400, 13%) | -18% (2069, 5%) | -39% (13, 8%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1400, 14%) | -18% (2069, 5%) | -45% (13, 8%) | -26% (75, 37%) |
| sl30_tp50 | -64% (1400, 16%) | -18% (2069, 6%) | -41% (13, 8%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1400, 17%) | -18% (2069, 6%) | -48% (13, 8%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1400, 15%) | -19% (2069, 5%) | -43% (13, 8%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 53215. Outcomes:

- missed_window: 35483
- low_liquidity: 8518
- proven_liquidity_gone: 3944
- no_momentum: 2129
- research_failed: 1421
- proven_low_volume: 823
- simulated failed buy: 672
- proven_price_collapsed_or_parabolic: 89
- proven: 75
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 459 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
