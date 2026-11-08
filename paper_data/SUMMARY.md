# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T08:17:59Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1121 | 13% | -62.1% | -66 to -58 | -69762 |
| all momentum | 1137 | 13% | -61.7% | -65 to -58 | -70305 |
| control | 1497 | 6% | -19.1% | -21 to -17 | -28774 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1116, 13%) | -19% (1497, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -62% (1116, 15%) | -19% (1497, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -63% (1116, 16%) | -19% (1497, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -63% (1116, 18%) | -20% (1497, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -62% (1116, 16%) | -20% (1497, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 40591. Outcomes:

- missed_window: 26543
- low_liquidity: 7052
- proven_liquidity_gone: 3131
- no_momentum: 1548
- research_failed: 1132
- proven_low_volume: 520
- simulated failed buy: 487
- proven_price_collapsed_or_parabolic: 71
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 304 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
