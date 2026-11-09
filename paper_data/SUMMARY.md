# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T13:34:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1322 | 13% | -63.2% | -66 to -60 | -83605 |
| all momentum | 1338 | 13% | -62.8% | -66 to -60 | -84148 |
| control | 1850 | 5% | -18.7% | -20 to -17 | -34790 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 65 | 43% | -19.4% | -31 to -7 | -1266 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1317, 13%) | -19% (1850, 5%) | -39% (13, 8%) | -19% (65, 43%) |
| wide_sl50_tp100 | -63% (1317, 15%) | -19% (1850, 6%) | -45% (13, 8%) | -20% (65, 43%) |
| sl30_tp50 | -64% (1317, 16%) | -19% (1850, 6%) | -41% (13, 8%) | -21% (65, 43%) |
| sl50_tp50 | -64% (1317, 18%) | -19% (1850, 6%) | -48% (13, 8%) | -21% (65, 43%) |
| no_stop_tp100 | -62% (1317, 15%) | -19% (1850, 6%) | -43% (13, 8%) | -20% (65, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 49354. Outcomes:

- missed_window: 32766
- low_liquidity: 8090
- proven_liquidity_gone: 3747
- no_momentum: 1904
- research_failed: 1332
- proven_low_volume: 710
- simulated failed buy: 599
- proven_price_collapsed_or_parabolic: 83
- proven: 65
- proven_no_uptrend: 29
- research_passed: 16
- dip: 13

Warning: 399 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
