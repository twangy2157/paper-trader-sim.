# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T04:19:10Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 29. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 588 | 16% | -53.8% | -59 to -49 | -31674 |
| all momentum | 593 | 16% | -53.6% | -59 to -49 | -31857 |
| control | 712 | 7% | -19.0% | -22 to -16 | -13575 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (572, 16%) | -19% (712, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -54% (572, 18%) | -20% (712, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (572, 20%) | -19% (712, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -55% (572, 22%) | -20% (712, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -53% (572, 19%) | -20% (712, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21324. Outcomes:

- missed_window: 13981
- low_liquidity: 3953
- proven_liquidity_gone: 1457
- no_momentum: 773
- research_failed: 598
- simulated failed buy: 239
- proven_low_volume: 214
- proven_price_collapsed_or_parabolic: 46
- proven: 34
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 160 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
