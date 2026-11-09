# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T10:19:55Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 76.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1298 | 13% | -63.3% | -67 to -60 | -82267 |
| all momentum | 1314 | 13% | -62.9% | -66 to -60 | -82811 |
| control | 1814 | 5% | -18.7% | -20 to -17 | -34038 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 61 | 44% | -16.9% | -29 to -5 | -1036 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1293, 13%) | -19% (1814, 5%) | -39% (13, 8%) | -17% (61, 44%) |
| wide_sl50_tp100 | -63% (1293, 14%) | -19% (1814, 6%) | -45% (13, 8%) | -17% (61, 44%) |
| sl30_tp50 | -64% (1293, 16%) | -19% (1814, 6%) | -41% (13, 8%) | -18% (61, 44%) |
| sl50_tp50 | -64% (1293, 18%) | -19% (1814, 6%) | -48% (13, 8%) | -18% (61, 44%) |
| no_stop_tp100 | -63% (1293, 15%) | -19% (1814, 6%) | -43% (13, 8%) | -17% (61, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 48410. Outcomes:

- missed_window: 32124
- low_liquidity: 7955
- proven_liquidity_gone: 3674
- no_momentum: 1868
- research_failed: 1302
- proven_low_volume: 697
- simulated failed buy: 587
- proven_price_collapsed_or_parabolic: 82
- proven: 64
- proven_no_uptrend: 28
- research_passed: 16
- dip: 13

Warning: 387 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
