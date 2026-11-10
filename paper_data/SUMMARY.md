# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T10:45:44Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 52.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1485 | 12% | -63.6% | -66 to -61 | -94603 |
| all momentum | 1501 | 12% | -63.3% | -66 to -60 | -95146 |
| control | 2177 | 5% | -18.1% | -19 to -17 | -39497 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 76 | 37% | -25.8% | -37 to -14 | -1965 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1480, 13%) | -18% (2177, 5%) | -33% (15, 13%) | -26% (76, 37%) |
| wide_sl50_tp100 | -63% (1480, 14%) | -18% (2177, 5%) | -39% (15, 13%) | -27% (76, 37%) |
| sl30_tp50 | -65% (1480, 15%) | -18% (2177, 6%) | -37% (15, 13%) | -27% (76, 37%) |
| sl50_tp50 | -64% (1480, 17%) | -19% (2177, 6%) | -43% (15, 13%) | -28% (76, 37%) |
| no_stop_tp100 | -63% (1480, 15%) | -19% (2177, 5%) | -35% (15, 13%) | -27% (76, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 55666. Outcomes:

- missed_window: 37094
- low_liquidity: 8868
- proven_liquidity_gone: 4168
- no_momentum: 2229
- research_failed: 1494
- proven_low_volume: 873
- simulated failed buy: 699
- proven_price_collapsed_or_parabolic: 97
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 15

Warning: 470 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
