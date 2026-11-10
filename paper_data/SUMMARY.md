# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T13:29:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 10. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1508 | 12% | -63.6% | -66 to -61 | -96028 |
| all momentum | 1524 | 12% | -63.3% | -66 to -60 | -96571 |
| control | 2208 | 5% | -18.0% | -20 to -17 | -40012 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1503, 13%) | -18% (2208, 5%) | -33% (15, 13%) | -26% (78, 37%) |
| wide_sl50_tp100 | -63% (1503, 14%) | -18% (2208, 5%) | -39% (15, 13%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1503, 15%) | -18% (2208, 6%) | -37% (15, 13%) | -28% (78, 37%) |
| sl50_tp50 | -64% (1503, 17%) | -19% (2208, 6%) | -43% (15, 13%) | -28% (78, 37%) |
| no_stop_tp100 | -63% (1503, 15%) | -19% (2208, 5%) | -35% (15, 13%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 56325. Outcomes:

- missed_window: 37530
- low_liquidity: 8962
- proven_liquidity_gone: 4232
- no_momentum: 2259
- research_failed: 1510
- proven_low_volume: 883
- simulated failed buy: 705
- proven_price_collapsed_or_parabolic: 99
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 474 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
