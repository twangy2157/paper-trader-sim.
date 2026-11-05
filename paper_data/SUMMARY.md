# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T03:03:32Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 13. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 580 | 15% | -54.6% | -60 to -50 | -31728 |
| all momentum | 585 | 15% | -54.5% | -59 to -49 | -31912 |
| control | 704 | 7% | -19.3% | -22 to -17 | -13661 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (564, 16%) | -19% (704, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -55% (564, 18%) | -20% (704, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (564, 19%) | -20% (704, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -56% (564, 22%) | -20% (704, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -54% (564, 19%) | -20% (704, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21042. Outcomes:

- missed_window: 13829
- low_liquidity: 3892
- proven_liquidity_gone: 1428
- no_momentum: 756
- research_failed: 585
- simulated failed buy: 236
- proven_low_volume: 211
- proven_price_collapsed_or_parabolic: 44
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 158 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
