# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T02:45:59Z. Bankroll cash (research-selected trades): 299.447018489884. Open positions: 39. Pools on watchlist: 68.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 15 | 20% | -39.9% | -69 to -10 | -601 |
| momentum, not picked | 1077 | 13% | -62.0% | -65 to -58 | -66824 |
| all momentum | 1092 | 13% | -61.6% | -65 to -58 | -67425 |
| control | 1431 | 6% | -19.6% | -22 to -18 | -28157 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 55 | 47% | -14.9% | -27 to -2 | -826 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1071, 13%) | -20% (1431, 6%) | -41% (11, 9%) | -15% (55, 47%) |
| wide_sl50_tp100 | -62% (1071, 15%) | -20% (1431, 6%) | -48% (11, 9%) | -15% (55, 47%) |
| sl30_tp50 | -63% (1071, 16%) | -20% (1431, 7%) | -44% (11, 9%) | -17% (55, 47%) |
| sl50_tp50 | -63% (1071, 18%) | -20% (1431, 7%) | -52% (11, 9%) | -17% (55, 47%) |
| no_stop_tp100 | -62% (1071, 15%) | -20% (1431, 6%) | -45% (11, 9%) | -15% (55, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 39147. Outcomes:

- missed_window: 25582
- low_liquidity: 6836
- proven_liquidity_gone: 3002
- no_momentum: 1498
- research_failed: 1092
- proven_low_volume: 489
- simulated failed buy: 474
- proven_price_collapsed_or_parabolic: 68
- proven: 55
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 300 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
