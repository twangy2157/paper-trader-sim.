# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T08:39:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1126 | 13% | -62.3% | -66 to -59 | -70262 |
| all momentum | 1142 | 13% | -61.9% | -65 to -58 | -70806 |
| control | 1499 | 6% | -19.1% | -21 to -17 | -28784 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1121, 13%) | -19% (1499, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -62% (1121, 15%) | -19% (1499, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -64% (1121, 16%) | -19% (1499, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -63% (1121, 18%) | -20% (1499, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -62% (1121, 15%) | -20% (1499, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 40685. Outcomes:

- missed_window: 26598
- low_liquidity: 7069
- proven_liquidity_gone: 3140
- no_momentum: 1555
- research_failed: 1134
- proven_low_volume: 523
- simulated failed buy: 488
- proven_price_collapsed_or_parabolic: 71
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 305 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
