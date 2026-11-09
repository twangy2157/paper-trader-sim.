# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T19:23:32Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 77.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1361 | 13% | -63.4% | -67 to -60 | -86439 |
| all momentum | 1377 | 13% | -63.1% | -66 to -60 | -86983 |
| control | 1938 | 5% | -18.5% | -20 to -17 | -36100 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 74 | 38% | -26.0% | -38 to -14 | -1931 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1356, 13%) | -19% (1938, 5%) | -39% (13, 8%) | -26% (74, 38%) |
| wide_sl50_tp100 | -63% (1356, 14%) | -19% (1938, 6%) | -45% (13, 8%) | -26% (74, 38%) |
| sl30_tp50 | -64% (1356, 16%) | -19% (1938, 6%) | -41% (13, 8%) | -27% (74, 38%) |
| sl50_tp50 | -64% (1356, 17%) | -19% (1938, 6%) | -48% (13, 8%) | -28% (74, 38%) |
| no_stop_tp100 | -63% (1356, 15%) | -19% (1938, 6%) | -43% (13, 8%) | -27% (74, 38%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 51269. Outcomes:

- missed_window: 34180
- low_liquidity: 8253
- proven_liquidity_gone: 3858
- no_momentum: 2000
- research_failed: 1364
- proven_low_volume: 758
- simulated failed buy: 635
- proven_price_collapsed_or_parabolic: 86
- proven: 74
- proven_no_uptrend: 32
- research_passed: 16
- dip: 13

Warning: 430 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
