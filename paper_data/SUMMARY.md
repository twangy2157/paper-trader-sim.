# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T03:28:32Z. Bankroll cash (research-selected trades): 299.447018489884. Open positions: 30. Pools on watchlist: 52.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 15 | 20% | -39.9% | -69 to -10 | -601 |
| momentum, not picked | 1088 | 13% | -62.0% | -66 to -58 | -67591 |
| all momentum | 1103 | 13% | -61.7% | -65 to -58 | -68192 |
| control | 1442 | 6% | -19.5% | -21 to -18 | -28248 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 55 | 47% | -14.9% | -27 to -2 | -826 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1082, 13%) | -20% (1442, 6%) | -41% (11, 9%) | -15% (55, 47%) |
| wide_sl50_tp100 | -62% (1082, 15%) | -20% (1442, 6%) | -48% (11, 9%) | -15% (55, 47%) |
| sl30_tp50 | -63% (1082, 16%) | -20% (1442, 7%) | -44% (11, 9%) | -17% (55, 47%) |
| sl50_tp50 | -63% (1082, 18%) | -20% (1442, 7%) | -52% (11, 9%) | -17% (55, 47%) |
| no_stop_tp100 | -62% (1082, 15%) | -20% (1442, 6%) | -45% (11, 9%) | -15% (55, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 39355. Outcomes:

- missed_window: 25728
- low_liquidity: 6864
- proven_liquidity_gone: 3015
- no_momentum: 1508
- research_failed: 1095
- proven_low_volume: 495
- simulated failed buy: 474
- proven_price_collapsed_or_parabolic: 70
- proven: 55
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 300 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
