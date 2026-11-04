# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T20:11:40Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 19. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 524 | 16% | -52.8% | -58 to -47 | -27719 |
| all momentum | 529 | 16% | -52.7% | -58 to -47 | -27902 |
| control | 634 | 7% | -19.0% | -22 to -16 | -12083 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 29 | 41% | -18.2% | -37 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (508, 16%) | -19% (634, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| wide_sl50_tp100 | -53% (508, 19%) | -19% (634, 8%) | -13% (4, 25%) | -18% (29, 41%) |
| sl30_tp50 | -55% (508, 20%) | -19% (634, 8%) | -22% (4, 25%) | -20% (29, 41%) |
| sl50_tp50 | -54% (508, 23%) | -19% (634, 9%) | -22% (4, 25%) | -20% (29, 41%) |
| no_stop_tp100 | -52% (508, 20%) | -20% (634, 8%) | -13% (4, 25%) | -18% (29, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 19434. Outcomes:

- missed_window: 12842
- low_liquidity: 3592
- proven_liquidity_gone: 1277
- no_momentum: 691
- research_failed: 529
- simulated failed buy: 222
- proven_low_volume: 182
- proven_price_collapsed_or_parabolic: 40
- proven: 30
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 150 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
