# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T13:56:14Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1326 | 13% | -63.0% | -66 to -60 | -83667 |
| all momentum | 1342 | 13% | -62.7% | -66 to -59 | -84210 |
| control | 1854 | 5% | -18.7% | -20 to -17 | -34903 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 65 | 43% | -19.4% | -31 to -7 | -1266 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1321, 13%) | -19% (1854, 5%) | -39% (13, 8%) | -19% (65, 43%) |
| wide_sl50_tp100 | -63% (1321, 15%) | -19% (1854, 6%) | -45% (13, 8%) | -20% (65, 43%) |
| sl30_tp50 | -64% (1321, 16%) | -19% (1854, 6%) | -41% (13, 8%) | -21% (65, 43%) |
| sl50_tp50 | -63% (1321, 18%) | -19% (1854, 6%) | -48% (13, 8%) | -21% (65, 43%) |
| no_stop_tp100 | -62% (1321, 15%) | -19% (1854, 6%) | -43% (13, 8%) | -20% (65, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 49471. Outcomes:

- missed_window: 32859
- low_liquidity: 8099
- proven_liquidity_gone: 3751
- no_momentum: 1905
- research_failed: 1335
- proven_low_volume: 712
- simulated failed buy: 599
- proven_price_collapsed_or_parabolic: 83
- proven: 69
- proven_no_uptrend: 30
- research_passed: 16
- dip: 13

Warning: 399 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
