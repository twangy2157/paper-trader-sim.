# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T09:54:44Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 11. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1138 | 13% | -62.7% | -66 to -59 | -71466 |
| all momentum | 1154 | 13% | -62.3% | -66 to -59 | -72010 |
| control | 1512 | 6% | -19.2% | -21 to -17 | -29087 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1133, 13%) | -19% (1512, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1133, 14%) | -20% (1512, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -64% (1133, 16%) | -19% (1512, 7%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -63% (1133, 18%) | -20% (1512, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1133, 15%) | -20% (1512, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 41019. Outcomes:

- missed_window: 26822
- low_liquidity: 7124
- proven_liquidity_gone: 3170
- no_momentum: 1559
- research_failed: 1146
- proven_low_volume: 526
- simulated failed buy: 494
- proven_price_collapsed_or_parabolic: 71
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 309 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
