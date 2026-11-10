# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T14:23:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 60. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1509 | 12% | -63.5% | -67 to -61 | -96029 |
| all momentum | 1525 | 12% | -63.2% | -66 to -60 | -96573 |
| control | 2212 | 5% | -18.0% | -19 to -17 | -40047 |
| dip buy | 15 | 13% | -32.7% | -58 to -8 | -491 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1504, 13%) | -18% (2212, 5%) | -33% (15, 13%) | -26% (78, 37%) |
| wide_sl50_tp100 | -63% (1504, 14%) | -18% (2212, 5%) | -39% (15, 13%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1504, 15%) | -18% (2212, 6%) | -37% (15, 13%) | -28% (78, 37%) |
| sl50_tp50 | -64% (1504, 17%) | -18% (2212, 6%) | -43% (15, 13%) | -28% (78, 37%) |
| no_stop_tp100 | -63% (1504, 15%) | -19% (2212, 5%) | -35% (15, 13%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 56667. Outcomes:

- missed_window: 37702
- low_liquidity: 9038
- proven_liquidity_gone: 4260
- no_momentum: 2282
- research_failed: 1542
- proven_low_volume: 887
- simulated failed buy: 712
- proven_price_collapsed_or_parabolic: 99
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 481 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
