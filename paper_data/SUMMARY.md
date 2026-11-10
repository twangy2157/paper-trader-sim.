# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-10T00:04:37Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1399 | 12% | -63.4% | -66 to -60 | -88895 |
| all momentum | 1415 | 13% | -63.1% | -66 to -60 | -89438 |
| control | 2060 | 5% | -18.0% | -20 to -17 | -37315 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 75 | 37% | -25.7% | -37 to -14 | -1933 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1394, 13%) | -18% (2060, 5%) | -39% (13, 8%) | -26% (75, 37%) |
| wide_sl50_tp100 | -63% (1394, 14%) | -18% (2060, 5%) | -45% (13, 8%) | -26% (75, 37%) |
| sl30_tp50 | -64% (1394, 16%) | -18% (2060, 6%) | -41% (13, 8%) | -27% (75, 37%) |
| sl50_tp50 | -64% (1394, 17%) | -18% (2060, 6%) | -48% (13, 8%) | -27% (75, 37%) |
| no_stop_tp100 | -63% (1394, 15%) | -19% (2060, 5%) | -43% (13, 8%) | -27% (75, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 53017. Outcomes:

- missed_window: 35362
- low_liquidity: 8490
- proven_liquidity_gone: 3930
- no_momentum: 2114
- research_failed: 1409
- proven_low_volume: 818
- simulated failed buy: 670
- proven_price_collapsed_or_parabolic: 88
- proven: 75
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 459 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
