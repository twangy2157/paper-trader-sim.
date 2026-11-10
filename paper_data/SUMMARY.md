# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T05:07:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 34. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1437 | 12% | -63.5% | -66 to -60 | -91373 |
| all momentum | 1453 | 12% | -63.2% | -66 to -60 | -91917 |
| control | 2117 | 5% | -18.1% | -20 to -17 | -38454 |
| dip buy | 14 | 14% | -31.9% | -58 to -5 | -447 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1432, 12%) | -18% (2117, 5%) | -32% (14, 14%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1432, 14%) | -18% (2117, 5%) | -38% (14, 14%) | -26% (75, 37%) |
| sl30_tp50 | -64% (1432, 15%) | -18% (2117, 6%) | -37% (14, 14%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1432, 17%) | -19% (2117, 6%) | -43% (14, 14%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1432, 15%) | -19% (2117, 5%) | -36% (14, 14%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 54367. Outcomes:

- missed_window: 36260
- low_liquidity: 8678
- proven_liquidity_gone: 4035
- no_momentum: 2178
- research_failed: 1453
- proven_low_volume: 847
- simulated failed buy: 685
- proven_price_collapsed_or_parabolic: 93
- proven: 76
- proven_no_uptrend: 32
- research_passed: 16
- dip: 14

Warning: 465 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
