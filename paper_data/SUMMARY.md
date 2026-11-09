# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T21:22:21Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 52. Pools on watchlist: 98.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1369 | 12% | -63.6% | -67 to -61 | -87138 |
| all momentum | 1385 | 13% | -63.2% | -66 to -60 | -87681 |
| control | 1985 | 5% | -18.4% | -20 to -17 | -36660 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 74 | 38% | -26.0% | -38 to -14 | -1931 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1364, 13%) | -18% (1985, 5%) | -39% (13, 8%) | -26% (74, 38%) |
| wide_sl50_tp100 | -63% (1364, 14%) | -19% (1985, 6%) | -45% (13, 8%) | -26% (74, 38%) |
| sl30_tp50 | -65% (1364, 16%) | -19% (1985, 6%) | -41% (13, 8%) | -27% (74, 38%) |
| sl50_tp50 | -64% (1364, 17%) | -19% (1985, 6%) | -48% (13, 8%) | -28% (74, 38%) |
| no_stop_tp100 | -63% (1364, 15%) | -19% (1985, 6%) | -43% (13, 8%) | -27% (74, 38%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 52061. Outcomes:

- missed_window: 34727
- low_liquidity: 8339
- proven_liquidity_gone: 3890
- no_momentum: 2067
- research_failed: 1382
- proven_low_volume: 782
- simulated failed buy: 651
- proven_price_collapsed_or_parabolic: 87
- proven: 75
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 442 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
