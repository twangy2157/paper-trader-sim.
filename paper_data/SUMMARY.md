# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T10:27:43Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1142 | 13% | -62.8% | -66 to -60 | -71866 |
| all momentum | 1158 | 13% | -62.4% | -66 to -59 | -72410 |
| control | 1514 | 6% | -19.1% | -21 to -17 | -29098 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 56 | 46% | -16.4% | -30 to -3 | -927 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1137, 13%) | -19% (1514, 6%) | -41% (11, 9%) | -16% (56, 46%) |
| wide_sl50_tp100 | -63% (1137, 14%) | -19% (1514, 6%) | -48% (11, 9%) | -16% (56, 46%) |
| sl30_tp50 | -64% (1137, 16%) | -19% (1514, 7%) | -44% (11, 9%) | -18% (56, 46%) |
| sl50_tp50 | -64% (1137, 18%) | -20% (1514, 7%) | -52% (11, 9%) | -18% (56, 46%) |
| no_stop_tp100 | -63% (1137, 15%) | -20% (1514, 6%) | -45% (11, 9%) | -16% (56, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 41171. Outcomes:

- missed_window: 26920
- low_liquidity: 7147
- proven_liquidity_gone: 3184
- no_momentum: 1568
- research_failed: 1149
- proven_low_volume: 529
- simulated failed buy: 496
- proven_price_collapsed_or_parabolic: 71
- proven: 56
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 311 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
