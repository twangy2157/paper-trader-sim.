# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T04:19:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 69.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1256 | 12% | -64.0% | -67 to -61 | -80530 |
| all momentum | 1272 | 12% | -63.6% | -67 to -60 | -81074 |
| control | 1745 | 5% | -18.6% | -20 to -17 | -32675 |
| dip buy | 12 | 8% | -39.5% | -67 to -12 | -474 |
| proven pools | 60 | 43% | -17.2% | -29 to -5 | -1039 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (1251, 12%) | -19% (1745, 5%) | -39% (12, 8%) | -17% (60, 43%) |
| wide_sl50_tp100 | -64% (1251, 14%) | -19% (1745, 6%) | -47% (12, 8%) | -17% (60, 43%) |
| sl30_tp50 | -65% (1251, 15%) | -19% (1745, 6%) | -42% (12, 8%) | -19% (60, 43%) |
| sl50_tp50 | -64% (1251, 17%) | -19% (1745, 7%) | -49% (12, 8%) | -19% (60, 43%) |
| no_stop_tp100 | -64% (1251, 15%) | -19% (1745, 6%) | -44% (12, 8%) | -17% (60, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 46954. Outcomes:

- missed_window: 31150
- low_liquidity: 7763
- proven_liquidity_gone: 3555
- no_momentum: 1800
- research_failed: 1263
- proven_low_volume: 660
- simulated failed buy: 568
- proven_price_collapsed_or_parabolic: 80
- proven: 60
- proven_no_uptrend: 27
- research_passed: 16
- dip: 12

Warning: 377 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
