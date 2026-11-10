# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T21:46:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1613 | 12% | -64.6% | -67 to -62 | -104315 |
| all momentum | 1629 | 12% | -64.3% | -67 to -61 | -104859 |
| control | 2345 | 5% | -18.0% | -19 to -17 | -42362 |
| dip buy | 17 | 24% | -20.2% | -47 to 8 | -345 |
| proven pools | 78 | 37% | -26.4% | -38 to -15 | -2065 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1608, 12%) | -18% (2345, 5%) | -20% (17, 24%) | -26% (78, 37%) |
| wide_sl50_tp100 | -64% (1608, 14%) | -18% (2345, 5%) | -26% (17, 24%) | -27% (78, 37%) |
| sl30_tp50 | -66% (1608, 15%) | -18% (2345, 6%) | -29% (17, 24%) | -28% (78, 37%) |
| sl50_tp50 | -65% (1608, 16%) | -19% (2345, 6%) | -34% (17, 24%) | -28% (78, 37%) |
| no_stop_tp100 | -64% (1608, 14%) | -19% (2345, 5%) | -22% (17, 24%) | -27% (78, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 58809. Outcomes:

- missed_window: 39004
- low_liquidity: 9427
- proven_liquidity_gone: 4432
- no_momentum: 2404
- research_failed: 1621
- proven_low_volume: 923
- simulated failed buy: 748
- proven_price_collapsed_or_parabolic: 102
- proven: 79
- proven_no_uptrend: 36
- dip: 17
- research_passed: 16

Warning: 501 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
