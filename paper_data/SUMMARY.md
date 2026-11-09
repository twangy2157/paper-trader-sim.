# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T03:59:08Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 13. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1253 | 12% | -64.1% | -67 to -61 | -80489 |
| all momentum | 1269 | 12% | -63.8% | -67 to -60 | -81033 |
| control | 1743 | 5% | -18.7% | -20 to -17 | -32698 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 60 | 43% | -17.2% | -29 to -5 | -1039 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1248, 12%) | -19% (1743, 5%) | -39% (12, 8%) | -17% (60, 43%) |
| wide_sl50_tp100 | -64% (1248, 14%) | -19% (1743, 6%) | -47% (12, 8%) | -17% (60, 43%) |
| sl30_tp50 | -65% (1248, 15%) | -19% (1743, 6%) | -42% (12, 8%) | -19% (60, 43%) |
| sl50_tp50 | -65% (1248, 17%) | -19% (1743, 6%) | -49% (12, 8%) | -19% (60, 43%) |
| no_stop_tp100 | -64% (1248, 15%) | -19% (1743, 6%) | -44% (12, 8%) | -17% (60, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 46867. Outcomes:

- missed_window: 31101
- low_liquidity: 7751
- proven_liquidity_gone: 3548
- no_momentum: 1794
- research_failed: 1259
- proven_low_volume: 655
- simulated failed buy: 565
- proven_price_collapsed_or_parabolic: 80
- proven: 60
- proven_no_uptrend: 26
- research_passed: 16
- dip: 12

Warning: 374 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
