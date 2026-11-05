# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T04:53:10Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 30. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 594 | 16% | -53.8% | -59 to -49 | -32005 |
| all momentum | 599 | 16% | -53.6% | -59 to -49 | -32188 |
| control | 717 | 7% | -19.1% | -22 to -16 | -13786 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 32 | 44% | -16.9% | -34 to -1 | -542 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (578, 16%) | -19% (717, 7%) | -13% (4, 25%) | -17% (32, 44%) |
| wide_sl50_tp100 | -54% (578, 18%) | -20% (717, 8%) | -13% (4, 25%) | -17% (32, 44%) |
| sl30_tp50 | -56% (578, 20%) | -20% (717, 8%) | -22% (4, 25%) | -18% (32, 44%) |
| sl50_tp50 | -55% (578, 22%) | -20% (717, 9%) | -22% (4, 25%) | -18% (32, 44%) |
| no_stop_tp100 | -53% (578, 19%) | -20% (717, 8%) | -13% (4, 25%) | -17% (32, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21474. Outcomes:

- missed_window: 14080
- low_liquidity: 3970
- proven_liquidity_gone: 1474
- no_momentum: 781
- research_failed: 601
- simulated failed buy: 241
- proven_low_volume: 217
- proven_price_collapsed_or_parabolic: 46
- proven: 35
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 161 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
