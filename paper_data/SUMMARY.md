# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T18:36:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 32. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1587 | 12% | -64.2% | -67 to -61 | -102023 |
| all momentum | 1603 | 12% | -63.9% | -67 to -61 | -102566 |
| control | 2293 | 5% | -18.0% | -19 to -17 | -41510 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1582, 12%) | -18% (2293, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1582, 14%) | -18% (2293, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1582, 15%) | -18% (2293, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1582, 17%) | -18% (2293, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1582, 14%) | -19% (2293, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 57912. Outcomes:

- missed_window: 38400
- low_liquidity: 9304
- proven_liquidity_gone: 4359
- no_momentum: 2358
- research_failed: 1598
- proven_low_volume: 909
- simulated failed buy: 738
- proven_price_collapsed_or_parabolic: 101
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 495 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
