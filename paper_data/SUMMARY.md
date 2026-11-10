# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T18:28:00Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 32. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1585 | 12% | -64.2% | -67 to -61 | -101918 |
| all momentum | 1601 | 12% | -63.9% | -67 to -61 | -102462 |
| control | 2291 | 5% | -18.0% | -19 to -17 | -41494 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1580, 12%) | -18% (2291, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1580, 14%) | -18% (2291, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1580, 15%) | -18% (2291, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1580, 17%) | -19% (2291, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1580, 14%) | -19% (2291, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 57870. Outcomes:

- missed_window: 38375
- low_liquidity: 9297
- proven_liquidity_gone: 4354
- no_momentum: 2355
- research_failed: 1597
- proven_low_volume: 909
- simulated failed buy: 737
- proven_price_collapsed_or_parabolic: 101
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 495 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
