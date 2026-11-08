# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T04:19:35Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1093 | 13% | -61.9% | -65 to -58 | -67769 |
| all momentum | 1109 | 13% | -61.5% | -65 to -58 | -68312 |
| control | 1462 | 6% | -19.3% | -21 to -17 | -28359 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 55 | 47% | -14.9% | -27 to -2 | -826 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -62% (1088, 13%) | -19% (1462, 6%) | -41% (11, 9%) | -15% (55, 47%) |
| wide_sl50_tp100 | -62% (1088, 15%) | -20% (1462, 6%) | -48% (11, 9%) | -15% (55, 47%) |
| sl30_tp50 | -63% (1088, 16%) | -20% (1462, 7%) | -44% (11, 9%) | -17% (55, 47%) |
| sl50_tp50 | -63% (1088, 18%) | -20% (1462, 7%) | -52% (11, 9%) | -17% (55, 47%) |
| no_stop_tp100 | -62% (1088, 16%) | -20% (1462, 6%) | -45% (11, 9%) | -15% (55, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 39615. Outcomes:

- missed_window: 25913
- low_liquidity: 6892
- proven_liquidity_gone: 3037
- no_momentum: 1518
- research_failed: 1096
- proven_low_volume: 506
- simulated failed buy: 477
- proven_price_collapsed_or_parabolic: 70
- proven: 55
- proven_no_uptrend: 24
- research_passed: 16
- dip: 11

Warning: 301 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
