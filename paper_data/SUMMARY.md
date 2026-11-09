# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T04:09:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1254 | 12% | -64.0% | -67 to -61 | -80396 |
| all momentum | 1270 | 12% | -63.6% | -67 to -60 | -80939 |
| control | 1744 | 5% | -18.7% | -20 to -17 | -32704 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 60 | 43% | -17.2% | -29 to -5 | -1039 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1249, 12%) | -19% (1744, 5%) | -39% (12, 8%) | -17% (60, 43%) |
| wide_sl50_tp100 | -64% (1249, 14%) | -19% (1744, 6%) | -47% (12, 8%) | -17% (60, 43%) |
| sl30_tp50 | -65% (1249, 15%) | -19% (1744, 6%) | -42% (12, 8%) | -19% (60, 43%) |
| sl50_tp50 | -64% (1249, 17%) | -19% (1744, 6%) | -49% (12, 8%) | -19% (60, 43%) |
| no_stop_tp100 | -64% (1249, 15%) | -19% (1744, 6%) | -44% (12, 8%) | -17% (60, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 46919. Outcomes:

- missed_window: 31133
- low_liquidity: 7756
- proven_liquidity_gone: 3553
- no_momentum: 1798
- research_failed: 1261
- proven_low_volume: 656
- simulated failed buy: 567
- proven_price_collapsed_or_parabolic: 80
- proven: 60
- proven_no_uptrend: 27
- research_passed: 16
- dip: 12

Warning: 376 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
