# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T19:39:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 73.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1598 | 12% | -64.4% | -67 to -61 | -103124 |
| all momentum | 1614 | 12% | -64.1% | -67 to -61 | -103668 |
| control | 2314 | 5% | -18.0% | -19 to -17 | -41927 |
| dip buy | 16 | 19% | -24.9% | -52 to 4 | -400 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1593, 12%) | -18% (2314, 5%) | -25% (16, 19%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1593, 14%) | -18% (2314, 5%) | -31% (16, 19%) | -27% (78, 37%) |
| sl30_tp50 | -65% (1593, 15%) | -18% (2314, 6%) | -32% (16, 19%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1593, 17%) | -18% (2314, 6%) | -38% (16, 19%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1593, 14%) | -19% (2314, 5%) | -27% (16, 19%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 58187. Outcomes:

- missed_window: 38597
- low_liquidity: 9337
- proven_liquidity_gone: 4380
- no_momentum: 2369
- research_failed: 1603
- proven_low_volume: 913
- simulated failed buy: 740
- proven_price_collapsed_or_parabolic: 102
- proven: 78
- proven_no_uptrend: 36
- research_passed: 16
- dip: 16

Warning: 496 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
