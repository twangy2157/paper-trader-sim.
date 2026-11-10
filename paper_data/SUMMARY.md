# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T17:44:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 35. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1574 | 12% | -64.2% | -67 to -61 | -101148 |
| all momentum | 1590 | 12% | -63.9% | -67 to -61 | -101691 |
| control | 2275 | 5% | -18.1% | -20 to -17 | -41399 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1569, 12%) | -18% (2275, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1569, 14%) | -18% (2275, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1569, 15%) | -18% (2275, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1569, 17%) | -19% (2275, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1569, 15%) | -19% (2275, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 57619. Outcomes:

- missed_window: 38225
- low_liquidity: 9246
- proven_liquidity_gone: 4335
- no_momentum: 2341
- research_failed: 1587
- proven_low_volume: 905
- simulated failed buy: 734
- proven_price_collapsed_or_parabolic: 101
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 493 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
