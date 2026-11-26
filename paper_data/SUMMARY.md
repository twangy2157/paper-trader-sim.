# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-26T12:27:57Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 27. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3850 | 12% | -65.6% | -67 to -64 | -252951 |
| all momentum | 3873 | 12% | -65.3% | -67 to -63 | -253339 |
| control | 4634 | 6% | -19.4% | -21 to -18 | -90302 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 135 | 33% | -31.2% | -40 to -23 | -4223 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (3852, 12%) | -19% (4634, 6%) | -13% (47, 28%) | -31% (135, 33%) |
| wide_sl50_tp100 | -65% (3852, 13%) | -20% (4634, 6%) | -13% (47, 32%) | -32% (135, 33%) |
| sl30_tp50 | -67% (3852, 14%) | -19% (4634, 7%) | -17% (47, 34%) | -31% (135, 33%) |
| sl50_tp50 | -67% (3852, 15%) | -20% (4634, 7%) | -18% (47, 38%) | -32% (135, 33%) |
| no_stop_tp100 | -65% (3852, 14%) | -20% (4634, 6%) | -12% (47, 32%) | -33% (135, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 124257. Outcomes:

- missed_window: 80093
- low_liquidity: 21333
- proven_liquidity_gone: 10667
- no_momentum: 4689
- research_failed: 3866
- simulated failed buy: 1584
- proven_low_volume: 1582
- proven_price_collapsed_or_parabolic: 169
- proven: 135
- proven_no_uptrend: 69
- dip: 47
- research_passed: 23

Warning: 978 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
