# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T04:57:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 32. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1436 | 12% | -63.5% | -67 to -60 | -91273 |
| all momentum | 1452 | 12% | -63.1% | -66 to -60 | -91817 |
| control | 2115 | 5% | -18.1% | -20 to -17 | -38434 |
| dip buy | 14 | 14% | -31.9% | -58 to -5 | -447 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1431, 13%) | -18% (2115, 5%) | -32% (14, 14%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1431, 14%) | -18% (2115, 5%) | -38% (14, 14%) | -26% (75, 37%) |
| sl30_tp50 | -64% (1431, 15%) | -18% (2115, 6%) | -37% (14, 14%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1431, 17%) | -19% (2115, 6%) | -43% (14, 14%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1431, 15%) | -19% (2115, 5%) | -36% (14, 14%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 54332. Outcomes:

- missed_window: 36241
- low_liquidity: 8673
- proven_liquidity_gone: 4033
- no_momentum: 2175
- research_failed: 1451
- proven_low_volume: 844
- simulated failed buy: 684
- proven_price_collapsed_or_parabolic: 93
- proven: 76
- proven_no_uptrend: 32
- research_passed: 16
- dip: 14

Warning: 464 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
