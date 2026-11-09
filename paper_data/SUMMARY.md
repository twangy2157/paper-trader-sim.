# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T10:41:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1300 | 13% | -63.3% | -66 to -60 | -82432 |
| all momentum | 1316 | 13% | -63.0% | -66 to -60 | -82975 |
| control | 1819 | 5% | -18.7% | -20 to -17 | -34165 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 62 | 45% | -16.6% | -29 to -5 | -1034 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1295, 13%) | -19% (1819, 5%) | -39% (13, 8%) | -17% (62, 45%) |
| wide_sl50_tp100 | -63% (1295, 14%) | -19% (1819, 6%) | -45% (13, 8%) | -17% (62, 45%) |
| sl30_tp50 | -64% (1295, 16%) | -19% (1819, 6%) | -41% (13, 8%) | -18% (62, 45%) |
| sl50_tp50 | -64% (1295, 18%) | -19% (1819, 6%) | -48% (13, 8%) | -18% (62, 45%) |
| no_stop_tp100 | -63% (1295, 15%) | -19% (1819, 6%) | -43% (13, 8%) | -17% (62, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 48520. Outcomes:

- missed_window: 32201
- low_liquidity: 7969
- proven_liquidity_gone: 3687
- no_momentum: 1871
- research_failed: 1303
- proven_low_volume: 698
- simulated failed buy: 587
- proven_price_collapsed_or_parabolic: 82
- proven: 65
- proven_no_uptrend: 28
- research_passed: 16
- dip: 13

Warning: 387 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
