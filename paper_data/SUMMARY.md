# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T15:58:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 41. Pools on watchlist: 35.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1546 | 12% | -63.8% | -67 to -61 | -98839 |
| all momentum | 1562 | 12% | -63.5% | -66 to -61 | -99383 |
| control | 2241 | 5% | -18.0% | -19 to -17 | -40498 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1541, 13%) | -18% (2241, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1541, 14%) | -18% (2241, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1541, 15%) | -18% (2241, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -64% (1541, 17%) | -18% (2241, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -63% (1541, 15%) | -19% (2241, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 57159. Outcomes:

- missed_window: 38008
- low_liquidity: 9122
- proven_liquidity_gone: 4293
- no_momentum: 2309
- research_failed: 1563
- proven_low_volume: 897
- simulated failed buy: 723
- proven_price_collapsed_or_parabolic: 99
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 488 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
