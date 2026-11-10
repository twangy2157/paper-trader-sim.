# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T15:28:01Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 48. Pools on watchlist: 86.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1531 | 12% | -63.5% | -66 to -61 | -97435 |
| all momentum | 1547 | 13% | -63.2% | -66 to -60 | -97978 |
| control | 2233 | 5% | -18.0% | -19 to -17 | -40356 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1526, 13%) | -18% (2233, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -63% (1526, 14%) | -18% (2233, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1526, 15%) | -18% (2233, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -64% (1526, 17%) | -18% (2233, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -63% (1526, 15%) | -19% (2233, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 56988. Outcomes:

- missed_window: 37896
- low_liquidity: 9098
- proven_liquidity_gone: 4279
- no_momentum: 2297
- research_failed: 1559
- proven_low_volume: 894
- simulated failed buy: 721
- proven_price_collapsed_or_parabolic: 99
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 487 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
