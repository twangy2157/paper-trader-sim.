# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T18:16:44Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 32. Pools on watchlist: 100.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1584 | 12% | -64.2% | -67 to -61 | -101817 |
| all momentum | 1600 | 12% | -63.9% | -67 to -61 | -102360 |
| control | 2287 | 5% | -18.0% | -19 to -17 | -41461 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1579, 12%) | -18% (2287, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1579, 14%) | -18% (2287, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1579, 15%) | -18% (2287, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1579, 17%) | -19% (2287, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1579, 15%) | -19% (2287, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 57783. Outcomes:

- missed_window: 38318
- low_liquidity: 9282
- proven_liquidity_gone: 4348
- no_momentum: 2351
- research_failed: 1596
- proven_low_volume: 907
- simulated failed buy: 735
- proven_price_collapsed_or_parabolic: 101
- proven: 78
- proven_no_uptrend: 35
- research_passed: 16
- dip: 16

Warning: 494 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
