# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T22:52:30Z. Bankroll cash (research-selected trades): 499.4001435479087. Open positions: 31. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1057 | 13% | -61.3% | -65 to -58 | -64926 |
| all momentum | 1071 | 13% | -61.0% | -64 to -57 | -65426 |
| control | 1387 | 6% | -19.7% | -22 to -18 | -27395 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 54 | 48% | -15.1% | -29 to -3 | -820 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1050, 13%) | -20% (1387, 6%) | -41% (11, 9%) | -15% (54, 48%) |
| wide_sl50_tp100 | -61% (1050, 15%) | -20% (1387, 6%) | -48% (11, 9%) | -15% (54, 48%) |
| sl30_tp50 | -63% (1050, 16%) | -20% (1387, 7%) | -44% (11, 9%) | -17% (54, 48%) |
| sl50_tp50 | -62% (1050, 18%) | -20% (1387, 7%) | -52% (11, 9%) | -17% (54, 48%) |
| no_stop_tp100 | -61% (1050, 16%) | -20% (1387, 6%) | -45% (11, 9%) | -15% (54, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 37989. Outcomes:

- missed_window: 24741
- low_liquidity: 6705
- proven_liquidity_gone: 2952
- no_momentum: 1454
- research_failed: 1064
- simulated failed buy: 467
- proven_low_volume: 439
- proven_price_collapsed_or_parabolic: 63
- proven: 55
- proven_no_uptrend: 24
- research_passed: 14
- dip: 11

Warning: 295 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
