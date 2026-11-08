# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T19:41:20Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1209 | 12% | -63.7% | -67 to -60 | -77091 |
| all momentum | 1225 | 12% | -63.3% | -66 to -60 | -77635 |
| control | 1617 | 6% | -18.8% | -20 to -17 | -30602 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 57 | 46% | -16.2% | -30 to -4 | -932 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1204, 13%) | -19% (1617, 6%) | -39% (12, 8%) | -16% (57, 46%) |
| wide_sl50_tp100 | -64% (1204, 14%) | -19% (1617, 6%) | -47% (12, 8%) | -16% (57, 46%) |
| sl30_tp50 | -65% (1204, 16%) | -19% (1617, 6%) | -42% (12, 8%) | -18% (57, 46%) |
| sl50_tp50 | -64% (1204, 17%) | -19% (1617, 7%) | -49% (12, 8%) | -18% (57, 46%) |
| no_stop_tp100 | -63% (1204, 15%) | -20% (1617, 6%) | -44% (12, 8%) | -16% (57, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 43926. Outcomes:

- missed_window: 28855
- low_liquidity: 7490
- proven_liquidity_gone: 3384
- no_momentum: 1676
- research_failed: 1216
- proven_low_volume: 592
- simulated failed buy: 527
- proven_price_collapsed_or_parabolic: 75
- proven: 57
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 337 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
