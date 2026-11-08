# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T23:46:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 84.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1237 | 12% | -63.8% | -67 to -61 | -79036 |
| all momentum | 1253 | 12% | -63.4% | -67 to -60 | -79580 |
| control | 1689 | 5% | -18.6% | -20 to -17 | -31641 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 58 | 45% | -17.7% | -31 to -5 | -1032 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1232, 13%) | -19% (1689, 5%) | -39% (12, 8%) | -18% (58, 45%) |
| wide_sl50_tp100 | -64% (1232, 14%) | -19% (1689, 6%) | -47% (12, 8%) | -18% (58, 45%) |
| sl30_tp50 | -65% (1232, 15%) | -19% (1689, 6%) | -42% (12, 8%) | -19% (58, 45%) |
| sl50_tp50 | -64% (1232, 17%) | -19% (1689, 7%) | -49% (12, 8%) | -19% (58, 45%) |
| no_stop_tp100 | -63% (1232, 15%) | -19% (1689, 6%) | -44% (12, 8%) | -18% (58, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 45568. Outcomes:

- missed_window: 30145
- low_liquidity: 7607
- proven_liquidity_gone: 3470
- no_momentum: 1747
- research_failed: 1241
- proven_low_volume: 621
- simulated failed buy: 547
- proven_price_collapsed_or_parabolic: 76
- proven: 60
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 356 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
