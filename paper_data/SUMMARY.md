# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T02:24:38Z. Bankroll cash (research-selected trades): 399.447018489884. Open positions: 28. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 15 | 20% | -39.9% | -69 to -10 | -601 |
| momentum, not picked | 1074 | 13% | -61.8% | -65 to -58 | -66524 |
| all momentum | 1089 | 13% | -61.5% | -65 to -58 | -67124 |
| control | 1429 | 6% | -19.6% | -22 to -18 | -28147 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 55 | 47% | -14.9% | -27 to -2 | -826 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1068, 13%) | -20% (1429, 6%) | -41% (11, 9%) | -15% (55, 47%) |
| wide_sl50_tp100 | -62% (1068, 15%) | -20% (1429, 6%) | -48% (11, 9%) | -15% (55, 47%) |
| sl30_tp50 | -63% (1068, 16%) | -20% (1429, 7%) | -44% (11, 9%) | -17% (55, 47%) |
| sl50_tp50 | -63% (1068, 18%) | -20% (1429, 7%) | -52% (11, 9%) | -17% (55, 47%) |
| no_stop_tp100 | -62% (1068, 16%) | -20% (1429, 6%) | -45% (11, 9%) | -15% (55, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 39057. Outcomes:

- missed_window: 25533
- low_liquidity: 6812
- proven_liquidity_gone: 3002
- no_momentum: 1487
- research_failed: 1088
- proven_low_volume: 489
- simulated failed buy: 473
- proven_price_collapsed_or_parabolic: 68
- proven: 55
- proven_no_uptrend: 24
- research_passed: 15
- dip: 11

Warning: 299 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
