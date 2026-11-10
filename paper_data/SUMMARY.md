# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T06:00:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1451 | 12% | -63.6% | -66 to -61 | -92355 |
| all momentum | 1467 | 12% | -63.2% | -66 to -60 | -92898 |
| control | 2131 | 5% | -17.9% | -19 to -17 | -38430 |
| dip buy | 14 | 14% | -31.9% | -58 to -5 | -447 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1446, 13%) | -18% (2131, 5%) | -32% (14, 14%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1446, 14%) | -18% (2131, 5%) | -38% (14, 14%) | -26% (75, 37%) |
| sl30_tp50 | -64% (1446, 15%) | -18% (2131, 6%) | -37% (14, 14%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1446, 17%) | -18% (2131, 6%) | -43% (14, 14%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1446, 15%) | -19% (2131, 5%) | -36% (14, 14%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 54569. Outcomes:

- missed_window: 36392
- low_liquidity: 8702
- proven_liquidity_gone: 4054
- no_momentum: 2191
- research_failed: 1457
- proven_low_volume: 853
- simulated failed buy: 686
- proven_price_collapsed_or_parabolic: 94
- proven: 76
- proven_no_uptrend: 33
- research_passed: 16
- dip: 15

Warning: 465 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
