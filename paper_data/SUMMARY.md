# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-26T12:17:21Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 28. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3847 | 12% | -65.6% | -68 to -64 | -252650 |
| all momentum | 3870 | 12% | -65.3% | -67 to -63 | -253038 |
| control | 4634 | 6% | -19.4% | -21 to -18 | -90302 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3849, 12%) | -19% (4634, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3849, 13%) | -20% (4634, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3849, 14%) | -19% (4634, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3849, 15%) | -20% (4634, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3849, 14%) | -20% (4634, 6%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 124221. Outcomes:

- missed_window: 80075
- low_liquidity: 21324
- proven_liquidity_gone: 10661
- no_momentum: 4689
- research_failed: 3864
- simulated failed buy: 1584
- proven_low_volume: 1581
- proven_price_collapsed_or_parabolic: 169
- proven: 135
- proven_no_uptrend: 69
- dip: 47
- research_passed: 23

Warning: 978 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
