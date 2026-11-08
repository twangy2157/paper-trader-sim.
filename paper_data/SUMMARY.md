# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T09:32:08Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1134 | 13% | -62.6% | -66 to -59 | -71065 |
| all momentum | 1150 | 13% | -62.2% | -66 to -59 | -71609 |
| control | 1508 | 6% | -19.2% | -21 to -17 | -29065 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1129, 13%) | -19% (1508, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1129, 15%) | -20% (1508, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -64% (1129, 16%) | -19% (1508, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -63% (1129, 18%) | -20% (1508, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -62% (1129, 15%) | -20% (1508, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 40917. Outcomes:

- missed_window: 26754
- low_liquidity: 7111
- proven_liquidity_gone: 3157
- no_momentum: 1558
- research_failed: 1143
- proven_low_volume: 526
- simulated failed buy: 490
- proven_price_collapsed_or_parabolic: 71
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 306 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
