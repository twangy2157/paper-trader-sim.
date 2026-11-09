# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T02:33:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 25. Pools on watchlist: 71.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1244 | 12% | -64.0% | -67 to -61 | -79739 |
| all momentum | 1260 | 12% | -63.6% | -67 to -60 | -80282 |
| control | 1717 | 5% | -18.7% | -20 to -17 | -32198 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 60 | 43% | -17.2% | -29 to -5 | -1039 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1239, 13%) | -19% (1717, 5%) | -39% (12, 8%) | -17% (60, 43%) |
| wide_sl50_tp100 | -64% (1239, 14%) | -19% (1717, 6%) | -47% (12, 8%) | -17% (60, 43%) |
| sl30_tp50 | -65% (1239, 15%) | -19% (1717, 6%) | -42% (12, 8%) | -19% (60, 43%) |
| sl50_tp50 | -64% (1239, 17%) | -19% (1717, 6%) | -49% (12, 8%) | -19% (60, 43%) |
| no_stop_tp100 | -64% (1239, 15%) | -19% (1717, 6%) | -44% (12, 8%) | -17% (60, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 46392. Outcomes:

- missed_window: 30751
- low_liquidity: 7695
- proven_liquidity_gone: 3519
- no_momentum: 1778
- research_failed: 1252
- proven_low_volume: 647
- simulated failed buy: 556
- proven_price_collapsed_or_parabolic: 80
- proven: 60
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 365 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
