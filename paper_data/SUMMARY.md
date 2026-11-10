# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T14:33:43Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 61. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1511 | 12% | -63.6% | -66 to -61 | -96229 |
| all momentum | 1527 | 12% | -63.3% | -66 to -60 | -96773 |
| control | 2215 | 5% | -18.0% | -19 to -17 | -40055 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1506, 13%) | -18% (2215, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -63% (1506, 14%) | -18% (2215, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1506, 15%) | -18% (2215, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -64% (1506, 17%) | -18% (2215, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -63% (1506, 15%) | -19% (2215, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 56711. Outcomes:

- missed_window: 37720
- low_liquidity: 9052
- proven_liquidity_gone: 4263
- no_momentum: 2285
- research_failed: 1546
- proven_low_volume: 888
- simulated failed buy: 713
- proven_price_collapsed_or_parabolic: 99
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 481 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
