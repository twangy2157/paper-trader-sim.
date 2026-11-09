# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T17:40:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 25. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1354 | 13% | -63.5% | -66 to -60 | -86113 |
| all momentum | 1370 | 13% | -63.2% | -66 to -60 | -86656 |
| control | 1903 | 5% | -18.7% | -20 to -17 | -35758 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 71 | 39% | -24.9% | -37 to -13 | -1774 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1349, 13%) | -19% (1903, 5%) | -39% (13, 8%) | -25% (71, 39%) |
| wide_sl50_tp100 | -63% (1349, 14%) | -19% (1903, 6%) | -45% (13, 8%) | -25% (71, 39%) |
| sl30_tp50 | -64% (1349, 16%) | -19% (1903, 6%) | -41% (13, 8%) | -26% (71, 39%) |
| sl50_tp50 | -64% (1349, 17%) | -19% (1903, 6%) | -48% (13, 8%) | -27% (71, 39%) |
| no_stop_tp100 | -63% (1349, 15%) | -19% (1903, 6%) | -43% (13, 8%) | -25% (71, 39%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 50709. Outcomes:

- missed_window: 33766
- low_liquidity: 8212
- proven_liquidity_gone: 3829
- no_momentum: 1965
- research_failed: 1358
- proven_low_volume: 734
- simulated failed buy: 625
- proven_price_collapsed_or_parabolic: 86
- proven: 74
- proven_no_uptrend: 31
- research_passed: 16
- dip: 13

Warning: 420 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
