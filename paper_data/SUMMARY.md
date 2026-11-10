# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T18:04:58Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 35. Pools on watchlist: 76.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1581 | 12% | -64.1% | -67 to -61 | -101559 |
| all momentum | 1597 | 12% | -63.8% | -67 to -61 | -102102 |
| control | 2283 | 5% | -18.0% | -20 to -17 | -41398 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1576, 12%) | -18% (2283, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1576, 14%) | -18% (2283, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1576, 15%) | -18% (2283, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1576, 17%) | -19% (2283, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1576, 15%) | -19% (2283, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 57720. Outcomes:

- missed_window: 38276
- low_liquidity: 9271
- proven_liquidity_gone: 4342
- no_momentum: 2348
- research_failed: 1595
- proven_low_volume: 907
- simulated failed buy: 735
- proven_price_collapsed_or_parabolic: 101
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 494 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
