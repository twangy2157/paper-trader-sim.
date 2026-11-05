# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T02:32:43Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 18. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 574 | 15% | -54.6% | -59 to -49 | -31376 |
| all momentum | 579 | 15% | -54.4% | -60 to -49 | -31559 |
| control | 699 | 7% | -19.3% | -22 to -16 | -13535 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (558, 16%) | -19% (699, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -55% (558, 18%) | -20% (699, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (558, 20%) | -20% (699, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -56% (558, 22%) | -20% (699, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -54% (558, 19%) | -20% (699, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20890. Outcomes:

- missed_window: 13728
- low_liquidity: 3864
- proven_liquidity_gone: 1418
- no_momentum: 752
- research_failed: 583
- simulated failed buy: 231
- proven_low_volume: 209
- proven_price_collapsed_or_parabolic: 44
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 156 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
