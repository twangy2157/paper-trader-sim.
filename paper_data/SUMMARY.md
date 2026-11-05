# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T01:27:00Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 17. Pools on watchlist: 67.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 564 | 15% | -54.3% | -59 to -49 | -30662 |
| all momentum | 569 | 15% | -54.1% | -59 to -49 | -30845 |
| control | 691 | 7% | -19.3% | -22 to -16 | -13380 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 31 | 42% | -17.5% | -35 to -1 | -545 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (548, 16%) | -19% (691, 7%) | -13% (4, 25%) | -18% (31, 42%) |
| wide_sl50_tp100 | -55% (548, 18%) | -20% (691, 8%) | -13% (4, 25%) | -18% (31, 42%) |
| sl30_tp50 | -56% (548, 20%) | -20% (691, 8%) | -22% (4, 25%) | -19% (31, 42%) |
| sl50_tp50 | -55% (548, 22%) | -20% (691, 9%) | -22% (4, 25%) | -19% (31, 42%) |
| no_stop_tp100 | -54% (548, 19%) | -20% (691, 8%) | -13% (4, 25%) | -18% (31, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20575. Outcomes:

- missed_window: 13522
- low_liquidity: 3821
- proven_liquidity_gone: 1384
- no_momentum: 741
- research_failed: 574
- simulated failed buy: 230
- proven_low_volume: 198
- proven_price_collapsed_or_parabolic: 44
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 154 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
