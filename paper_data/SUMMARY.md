# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T09:01:22Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1130 | 13% | -62.4% | -66 to -59 | -70663 |
| all momentum | 1146 | 13% | -62.0% | -66 to -59 | -71207 |
| control | 1504 | 6% | -19.2% | -21 to -17 | -29038 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1125, 13%) | -19% (1504, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -62% (1125, 15%) | -20% (1504, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -64% (1125, 16%) | -19% (1504, 7%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -63% (1125, 18%) | -20% (1504, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -62% (1125, 15%) | -20% (1504, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 40778. Outcomes:

- missed_window: 26665
- low_liquidity: 7084
- proven_liquidity_gone: 3144
- no_momentum: 1556
- research_failed: 1138
- proven_low_volume: 524
- simulated failed buy: 489
- proven_price_collapsed_or_parabolic: 71
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 305 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
