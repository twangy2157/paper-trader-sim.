# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T20:11:27Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1601 | 12% | -64.4% | -67 to -62 | -103331 |
| all momentum | 1617 | 12% | -64.1% | -67 to -61 | -103875 |
| control | 2317 | 5% | -18.0% | -19 to -17 | -41941 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1596, 12%) | -18% (2317, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1596, 14%) | -18% (2317, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1596, 15%) | -18% (2317, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1596, 17%) | -19% (2317, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1596, 14%) | -19% (2317, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 58361. Outcomes:

- missed_window: 38704
- low_liquidity: 9371
- proven_liquidity_gone: 4394
- no_momentum: 2378
- research_failed: 1606
- proven_low_volume: 916
- simulated failed buy: 744
- proven_price_collapsed_or_parabolic: 102
- proven: 78
- proven_no_uptrend: 36
- research_passed: 16
- dip: 16

Warning: 496 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
