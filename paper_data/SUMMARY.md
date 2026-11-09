# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T15:33:50Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 34. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1342 | 13% | -63.4% | -67 to -60 | -85176 |
| all momentum | 1358 | 13% | -63.0% | -66 to -60 | -85719 |
| control | 1865 | 6% | -18.7% | -20 to -17 | -35139 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 65 | 43% | -19.4% | -31 to -7 | -1267 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1337, 13%) | -19% (1865, 6%) | -39% (13, 8%) | -19% (65, 43%) |
| wide_sl50_tp100 | -63% (1337, 14%) | -19% (1865, 6%) | -45% (13, 8%) | -20% (65, 43%) |
| sl30_tp50 | -64% (1337, 16%) | -19% (1865, 6%) | -41% (13, 8%) | -21% (65, 43%) |
| sl50_tp50 | -64% (1337, 18%) | -19% (1865, 7%) | -48% (13, 8%) | -21% (65, 43%) |
| no_stop_tp100 | -63% (1337, 15%) | -19% (1865, 6%) | -43% (13, 8%) | -20% (65, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 49999. Outcomes:

- missed_window: 33232
- low_liquidity: 8156
- proven_liquidity_gone: 3786
- no_momentum: 1927
- research_failed: 1349
- proven_low_volume: 718
- simulated failed buy: 614
- proven_price_collapsed_or_parabolic: 83
- proven: 74
- proven_no_uptrend: 31
- research_passed: 16
- dip: 13

Warning: 408 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
