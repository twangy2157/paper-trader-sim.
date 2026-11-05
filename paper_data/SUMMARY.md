# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T06:29:00Z. Bankroll cash (research-selected trades): 716.8065461812329. Open positions: 26. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 605 | 16% | -54.3% | -59 to -49 | -32875 |
| all momentum | 610 | 16% | -54.1% | -59 to -49 | -33058 |
| control | 741 | 8% | -18.8% | -21 to -16 | -14010 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (589, 16%) | -19% (741, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -55% (589, 18%) | -19% (741, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (589, 20%) | -19% (741, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -56% (589, 22%) | -19% (741, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -54% (589, 19%) | -19% (741, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21824. Outcomes:

- missed_window: 14290
- low_liquidity: 4033
- proven_liquidity_gone: 1509
- no_momentum: 792
- research_failed: 618
- simulated failed buy: 244
- proven_low_volume: 223
- proven_price_collapsed_or_parabolic: 48
- proven: 36
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 163 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
