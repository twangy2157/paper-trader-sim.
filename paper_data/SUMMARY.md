# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T21:54:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 47. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1374 | 12% | -63.5% | -66 to -60 | -87400 |
| all momentum | 1390 | 13% | -63.2% | -66 to -60 | -87943 |
| control | 2004 | 5% | -18.3% | -20 to -17 | -36872 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 74 | 38% | -26.0% | -38 to -14 | -1931 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1369, 13%) | -18% (2004, 5%) | -39% (13, 8%) | -26% (74, 38%) |
| wide_sl50_tp100 | -63% (1369, 14%) | -19% (2004, 6%) | -45% (13, 8%) | -26% (74, 38%) |
| sl30_tp50 | -64% (1369, 16%) | -19% (2004, 6%) | -41% (13, 8%) | -27% (74, 38%) |
| sl50_tp50 | -64% (1369, 17%) | -19% (2004, 6%) | -48% (13, 8%) | -28% (74, 38%) |
| no_stop_tp100 | -63% (1369, 15%) | -19% (2004, 6%) | -43% (13, 8%) | -27% (74, 38%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 52274. Outcomes:

- missed_window: 34873
- low_liquidity: 8374
- proven_liquidity_gone: 3898
- no_momentum: 2079
- research_failed: 1389
- proven_low_volume: 786
- simulated failed buy: 652
- proven_price_collapsed_or_parabolic: 87
- proven: 75
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 444 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
