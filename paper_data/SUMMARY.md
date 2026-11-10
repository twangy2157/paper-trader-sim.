# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T16:30:23Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 32. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1559 | 12% | -64.0% | -67 to -61 | -99994 |
| all momentum | 1575 | 12% | -63.7% | -67 to -61 | -100537 |
| control | 2252 | 5% | -18.0% | -19 to -17 | -40808 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1554, 12%) | -18% (2252, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1554, 14%) | -18% (2252, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1554, 15%) | -18% (2252, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1554, 17%) | -19% (2252, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1554, 15%) | -19% (2252, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 57286. Outcomes:

- missed_window: 38071
- low_liquidity: 9149
- proven_liquidity_gone: 4310
- no_momentum: 2315
- research_failed: 1572
- proven_low_volume: 900
- simulated failed buy: 725
- proven_price_collapsed_or_parabolic: 99
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 489 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
