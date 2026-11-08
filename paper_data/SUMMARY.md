# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T03:18:09Z. Bankroll cash (research-selected trades): 299.447018489884. Open positions: 30. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 15 | 20% | -39.9% | -69 to -10 | -601 |
| momentum, not picked | 1087 | 13% | -62.0% | -65 to -58 | -67491 |
| all momentum | 1102 | 13% | -61.7% | -65 to -58 | -68092 |
| control | 1439 | 6% | -19.5% | -21 to -18 | -28230 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 55 | 47% | -14.9% | -27 to -2 | -826 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1081, 13%) | -20% (1439, 6%) | -41% (11, 9%) | -15% (55, 47%) |
| wide_sl50_tp100 | -62% (1081, 15%) | -20% (1439, 6%) | -48% (11, 9%) | -15% (55, 47%) |
| sl30_tp50 | -63% (1081, 16%) | -20% (1439, 7%) | -44% (11, 9%) | -17% (55, 47%) |
| sl50_tp50 | -63% (1081, 18%) | -20% (1439, 7%) | -52% (11, 9%) | -17% (55, 47%) |
| no_stop_tp100 | -62% (1081, 15%) | -20% (1439, 6%) | -45% (11, 9%) | -15% (55, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 39310. Outcomes:

- missed_window: 25700
- low_liquidity: 6858
- proven_liquidity_gone: 3011
- no_momentum: 1506
- research_failed: 1093
- proven_low_volume: 493
- simulated failed buy: 474
- proven_price_collapsed_or_parabolic: 69
- proven: 55
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 300 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
