# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T15:55:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1180 | 12% | -63.3% | -66 to -60 | -74775 |
| all momentum | 1196 | 13% | -62.9% | -66 to -60 | -75319 |
| control | 1580 | 6% | -19.0% | -21 to -17 | -30134 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1175, 13%) | -19% (1580, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1175, 14%) | -19% (1580, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -65% (1175, 15%) | -19% (1580, 6%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1175, 17%) | -19% (1580, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1175, 15%) | -20% (1580, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 42717. Outcomes:

- missed_window: 27975
- low_liquidity: 7362
- proven_liquidity_gone: 3309
- no_momentum: 1633
- research_failed: 1187
- proven_low_volume: 561
- simulated failed buy: 509
- proven_price_collapsed_or_parabolic: 73
- proven: 57
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 319 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
