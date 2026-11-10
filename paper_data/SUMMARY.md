# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T05:18:01Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 32. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1439 | 12% | -63.5% | -66 to -61 | -91573 |
| all momentum | 1455 | 12% | -63.2% | -66 to -60 | -92117 |
| control | 2121 | 5% | -18.0% | -20 to -17 | -38479 |
| dip buy | 14 | 14% | -31.9% | -58 to -5 | -447 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1434, 12%) | -18% (2121, 5%) | -32% (14, 14%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1434, 14%) | -18% (2121, 5%) | -38% (14, 14%) | -26% (75, 37%) |
| sl30_tp50 | -64% (1434, 15%) | -18% (2121, 6%) | -37% (14, 14%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1434, 17%) | -19% (2121, 6%) | -43% (14, 14%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1434, 15%) | -19% (2121, 5%) | -36% (14, 14%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 54402. Outcomes:

- missed_window: 36284
- low_liquidity: 8680
- proven_liquidity_gone: 4039
- no_momentum: 2180
- research_failed: 1455
- proven_low_volume: 848
- simulated failed buy: 685
- proven_price_collapsed_or_parabolic: 93
- proven: 76
- proven_no_uptrend: 32
- research_passed: 16
- dip: 14

Warning: 465 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
