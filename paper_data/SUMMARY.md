# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-08T20:23:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 26. Pools on watchlist: 76.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1213 | 12% | -63.8% | -67 to -60 | -77493 |
| all momentum | 1229 | 12% | -63.4% | -67 to -60 | -78037 |
| control | 1625 | 6% | -18.9% | -21 to -17 | -30845 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 57 | 46% | -16.2% | -30 to -4 | -932 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1208, 13%) | -19% (1625, 6%) | -39% (12, 8%) | -16% (57, 46%) |
| wide_sl50_tp100 | -64% (1208, 14%) | -19% (1625, 6%) | -47% (12, 8%) | -16% (57, 46%) |
| sl30_tp50 | -65% (1208, 15%) | -19% (1625, 6%) | -42% (12, 8%) | -18% (57, 46%) |
| sl50_tp50 | -64% (1208, 17%) | -19% (1625, 7%) | -49% (12, 8%) | -18% (57, 46%) |
| no_stop_tp100 | -63% (1208, 15%) | -20% (1625, 6%) | -44% (12, 8%) | -16% (57, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 44164. Outcomes:

- missed_window: 29022
- low_liquidity: 7518
- proven_liquidity_gone: 3403
- no_momentum: 1687
- research_failed: 1220
- proven_low_volume: 596
- simulated failed buy: 530
- proven_price_collapsed_or_parabolic: 76
- proven: 58
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 339 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
