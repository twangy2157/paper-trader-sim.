# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T21:11:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 54. Pools on watchlist: 82.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1367 | 13% | -63.5% | -67 to -60 | -86937 |
| all momentum | 1383 | 13% | -63.2% | -66 to -60 | -87480 |
| control | 1979 | 5% | -18.4% | -20 to -17 | -36611 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 74 | 38% | -26.0% | -38 to -14 | -1931 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1362, 13%) | -18% (1979, 5%) | -39% (13, 8%) | -26% (74, 38%) |
| wide_sl50_tp100 | -63% (1362, 14%) | -19% (1979, 6%) | -45% (13, 8%) | -26% (74, 38%) |
| sl30_tp50 | -64% (1362, 16%) | -19% (1979, 6%) | -41% (13, 8%) | -27% (74, 38%) |
| sl50_tp50 | -64% (1362, 17%) | -19% (1979, 6%) | -48% (13, 8%) | -28% (74, 38%) |
| no_stop_tp100 | -63% (1362, 15%) | -19% (1979, 6%) | -43% (13, 8%) | -27% (74, 38%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 51993. Outcomes:

- missed_window: 34677
- low_liquidity: 8335
- proven_liquidity_gone: 3886
- no_momentum: 2063
- research_failed: 1380
- proven_low_volume: 780
- simulated failed buy: 649
- proven_price_collapsed_or_parabolic: 87
- proven: 75
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 442 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
