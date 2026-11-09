# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T07:30:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 10. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1275 | 12% | -63.6% | -67 to -61 | -81177 |
| all momentum | 1291 | 13% | -63.2% | -66 to -60 | -81721 |
| control | 1784 | 5% | -18.6% | -20 to -17 | -33340 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 60 | 43% | -17.2% | -29 to -5 | -1039 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1270, 13%) | -19% (1784, 5%) | -39% (13, 8%) | -17% (60, 43%) |
| wide_sl50_tp100 | -63% (1270, 14%) | -19% (1784, 6%) | -45% (13, 8%) | -17% (60, 43%) |
| sl30_tp50 | -64% (1270, 16%) | -19% (1784, 6%) | -41% (13, 8%) | -19% (60, 43%) |
| sl50_tp50 | -64% (1270, 17%) | -19% (1784, 7%) | -48% (13, 8%) | -19% (60, 43%) |
| no_stop_tp100 | -63% (1270, 15%) | -19% (1784, 6%) | -43% (13, 8%) | -17% (60, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 47630. Outcomes:

- missed_window: 31612
- low_liquidity: 7843
- proven_liquidity_gone: 3607
- no_momentum: 1833
- research_failed: 1279
- proven_low_volume: 680
- simulated failed buy: 577
- proven_price_collapsed_or_parabolic: 82
- proven: 61
- proven_no_uptrend: 27
- research_passed: 16
- dip: 13

Warning: 382 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
