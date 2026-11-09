# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T12:37:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 67.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1313 | 13% | -63.3% | -66 to -60 | -83173 |
| all momentum | 1329 | 13% | -62.9% | -66 to -60 | -83717 |
| control | 1839 | 5% | -18.7% | -20 to -17 | -34552 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 64 | 44% | -19.2% | -32 to -7 | -1233 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1308, 13%) | -19% (1839, 5%) | -39% (13, 8%) | -19% (64, 44%) |
| wide_sl50_tp100 | -63% (1308, 14%) | -19% (1839, 6%) | -45% (13, 8%) | -19% (64, 44%) |
| sl30_tp50 | -64% (1308, 16%) | -19% (1839, 6%) | -41% (13, 8%) | -21% (64, 44%) |
| sl50_tp50 | -64% (1308, 18%) | -19% (1839, 6%) | -48% (13, 8%) | -21% (64, 44%) |
| no_stop_tp100 | -63% (1308, 15%) | -19% (1839, 6%) | -43% (13, 8%) | -19% (64, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 49047. Outcomes:

- missed_window: 32542
- low_liquidity: 8050
- proven_liquidity_gone: 3730
- no_momentum: 1895
- research_failed: 1324
- proven_low_volume: 705
- simulated failed buy: 595
- proven_price_collapsed_or_parabolic: 83
- proven: 65
- proven_no_uptrend: 29
- research_passed: 16
- dip: 13

Warning: 397 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
