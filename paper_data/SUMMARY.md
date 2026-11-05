# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T05:13:39Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 22. Pools on watchlist: 37.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 598 | 16% | -53.9% | -59 to -49 | -32312 |
| all momentum | 603 | 16% | -53.8% | -59 to -49 | -32495 |
| control | 725 | 7% | -19.0% | -22 to -16 | -13859 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (582, 16%) | -19% (725, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -54% (582, 18%) | -20% (725, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (582, 20%) | -20% (725, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -55% (582, 22%) | -20% (725, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -53% (582, 19%) | -20% (725, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21545. Outcomes:

- missed_window: 14128
- low_liquidity: 3985
- proven_liquidity_gone: 1476
- no_momentum: 783
- research_failed: 603
- simulated failed buy: 242
- proven_low_volume: 218
- proven_price_collapsed_or_parabolic: 46
- proven: 35
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 162 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
