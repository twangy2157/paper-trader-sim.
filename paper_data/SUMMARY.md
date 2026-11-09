# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T17:07:39Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1352 | 12% | -63.6% | -67 to -61 | -86112 |
| all momentum | 1368 | 13% | -63.3% | -66 to -60 | -86656 |
| control | 1895 | 5% | -18.7% | -20 to -17 | -35615 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 70 | 40% | -23.8% | -36 to -12 | -1673 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1347, 13%) | -19% (1895, 5%) | -39% (13, 8%) | -24% (70, 40%) |
| wide_sl50_tp100 | -63% (1347, 14%) | -19% (1895, 6%) | -45% (13, 8%) | -24% (70, 40%) |
| sl30_tp50 | -65% (1347, 16%) | -19% (1895, 6%) | -41% (13, 8%) | -25% (70, 40%) |
| sl50_tp50 | -64% (1347, 17%) | -19% (1895, 6%) | -48% (13, 8%) | -25% (70, 40%) |
| no_stop_tp100 | -63% (1347, 15%) | -19% (1895, 6%) | -43% (13, 8%) | -24% (70, 40%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 50556. Outcomes:

- missed_window: 33662
- low_liquidity: 8190
- proven_liquidity_gone: 3827
- no_momentum: 1952
- research_failed: 1354
- proven_low_volume: 730
- simulated failed buy: 622
- proven_price_collapsed_or_parabolic: 85
- proven: 74
- proven_no_uptrend: 31
- research_passed: 16
- dip: 13

Warning: 417 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
