# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T03:27:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 69.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1252 | 12% | -64.2% | -67 to -61 | -80485 |
| all momentum | 1268 | 12% | -63.8% | -67 to -61 | -81029 |
| control | 1733 | 5% | -18.6% | -20 to -17 | -32447 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 60 | 43% | -17.2% | -29 to -5 | -1039 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1247, 12%) | -19% (1733, 5%) | -39% (12, 8%) | -17% (60, 43%) |
| wide_sl50_tp100 | -64% (1247, 14%) | -19% (1733, 6%) | -47% (12, 8%) | -17% (60, 43%) |
| sl30_tp50 | -65% (1247, 15%) | -19% (1733, 6%) | -42% (12, 8%) | -19% (60, 43%) |
| sl50_tp50 | -65% (1247, 17%) | -19% (1733, 7%) | -49% (12, 8%) | -19% (60, 43%) |
| no_stop_tp100 | -64% (1247, 15%) | -19% (1733, 6%) | -44% (12, 8%) | -17% (60, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 46691. Outcomes:

- missed_window: 30979
- low_liquidity: 7727
- proven_liquidity_gone: 3531
- no_momentum: 1789
- research_failed: 1256
- proven_low_volume: 653
- simulated failed buy: 562
- proven_price_collapsed_or_parabolic: 80
- proven: 60
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 370 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
