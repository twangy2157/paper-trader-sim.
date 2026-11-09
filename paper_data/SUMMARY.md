# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T06:16:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 11. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1270 | 12% | -63.7% | -67 to -60 | -81020 |
| all momentum | 1286 | 13% | -63.3% | -66 to -60 | -81563 |
| control | 1779 | 5% | -18.6% | -20 to -17 | -33212 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 60 | 43% | -17.2% | -29 to -5 | -1039 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1265, 13%) | -19% (1779, 5%) | -39% (12, 8%) | -17% (60, 43%) |
| wide_sl50_tp100 | -64% (1265, 14%) | -19% (1779, 6%) | -47% (12, 8%) | -17% (60, 43%) |
| sl30_tp50 | -65% (1265, 16%) | -19% (1779, 6%) | -42% (12, 8%) | -19% (60, 43%) |
| sl50_tp50 | -64% (1265, 17%) | -19% (1779, 7%) | -49% (12, 8%) | -19% (60, 43%) |
| no_stop_tp100 | -63% (1265, 15%) | -19% (1779, 6%) | -44% (12, 8%) | -17% (60, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 47486. Outcomes:

- missed_window: 31516
- low_liquidity: 7827
- proven_liquidity_gone: 3596
- no_momentum: 1827
- research_failed: 1275
- proven_low_volume: 673
- simulated failed buy: 574
- proven_price_collapsed_or_parabolic: 81
- proven: 61
- proven_no_uptrend: 27
- research_passed: 16
- dip: 13

Warning: 380 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
