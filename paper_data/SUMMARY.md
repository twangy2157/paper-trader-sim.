# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T23:33:39Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 21. Pools on watchlist: 30.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 549 | 16% | -53.6% | -59 to -48 | -29451 |
| all momentum | 554 | 16% | -53.4% | -59 to -48 | -29634 |
| control | 673 | 7% | -19.0% | -22 to -16 | -12817 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 31 | 42% | -17.5% | -35 to -1 | -545 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (533, 16%) | -19% (673, 7%) | -13% (4, 25%) | -18% (31, 42%) |
| wide_sl50_tp100 | -54% (533, 18%) | -19% (673, 8%) | -13% (4, 25%) | -18% (31, 42%) |
| sl30_tp50 | -55% (533, 20%) | -19% (673, 8%) | -22% (4, 25%) | -19% (31, 42%) |
| sl50_tp50 | -55% (533, 23%) | -19% (673, 9%) | -22% (4, 25%) | -19% (31, 42%) |
| no_stop_tp100 | -53% (533, 19%) | -20% (673, 8%) | -13% (4, 25%) | -18% (31, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20261. Outcomes:

- missed_window: 13345
- low_liquidity: 3750
- proven_liquidity_gone: 1355
- no_momentum: 731
- research_failed: 555
- simulated failed buy: 229
- proven_low_volume: 193
- proven_price_collapsed_or_parabolic: 42
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 153 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
