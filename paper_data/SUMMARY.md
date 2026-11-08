# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T23:25:08Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 33. Pools on watchlist: 106.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1233 | 12% | -63.7% | -67 to -60 | -78636 |
| all momentum | 1249 | 12% | -63.3% | -66 to -60 | -79179 |
| control | 1678 | 5% | -18.7% | -20 to -17 | -31558 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 58 | 45% | -17.7% | -31 to -5 | -1032 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1228, 13%) | -19% (1678, 5%) | -39% (12, 8%) | -18% (58, 45%) |
| wide_sl50_tp100 | -64% (1228, 14%) | -19% (1678, 6%) | -47% (12, 8%) | -18% (58, 45%) |
| sl30_tp50 | -65% (1228, 15%) | -19% (1678, 6%) | -42% (12, 8%) | -19% (58, 45%) |
| sl50_tp50 | -64% (1228, 17%) | -19% (1678, 7%) | -49% (12, 8%) | -19% (58, 45%) |
| no_stop_tp100 | -63% (1228, 15%) | -19% (1678, 6%) | -44% (12, 8%) | -18% (58, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 45411. Outcomes:

- missed_window: 30009
- low_liquidity: 7601
- proven_liquidity_gone: 3461
- no_momentum: 1745
- research_failed: 1241
- proven_low_volume: 619
- simulated failed buy: 545
- proven_price_collapsed_or_parabolic: 76
- proven: 60
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 355 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
