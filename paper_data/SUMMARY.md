# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T06:36:55Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1272 | 12% | -63.6% | -67 to -60 | -80970 |
| all momentum | 1288 | 13% | -63.2% | -66 to -60 | -81513 |
| control | 1780 | 5% | -18.6% | -20 to -17 | -33219 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 60 | 43% | -17.2% | -29 to -5 | -1039 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1267, 13%) | -19% (1780, 5%) | -39% (12, 8%) | -17% (60, 43%) |
| wide_sl50_tp100 | -63% (1267, 14%) | -19% (1780, 6%) | -47% (12, 8%) | -17% (60, 43%) |
| sl30_tp50 | -64% (1267, 16%) | -19% (1780, 6%) | -42% (12, 8%) | -19% (60, 43%) |
| sl50_tp50 | -64% (1267, 17%) | -19% (1780, 7%) | -49% (12, 8%) | -19% (60, 43%) |
| no_stop_tp100 | -63% (1267, 15%) | -19% (1780, 6%) | -44% (12, 8%) | -17% (60, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 47575. Outcomes:

- missed_window: 31566
- low_liquidity: 7840
- proven_liquidity_gone: 3604
- no_momentum: 1833
- research_failed: 1279
- proven_low_volume: 678
- simulated failed buy: 577
- proven_price_collapsed_or_parabolic: 81
- proven: 61
- proven_no_uptrend: 27
- research_passed: 16
- dip: 13

Warning: 382 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
