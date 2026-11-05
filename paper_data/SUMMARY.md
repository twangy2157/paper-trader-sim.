# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T01:37:14Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 18. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 565 | 15% | -54.4% | -60 to -49 | -30762 |
| all momentum | 570 | 15% | -54.2% | -59 to -49 | -30945 |
| control | 692 | 7% | -19.3% | -22 to -16 | -13387 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 31 | 42% | -17.5% | -35 to -1 | -545 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (549, 16%) | -19% (692, 7%) | -13% (4, 25%) | -18% (31, 42%) |
| wide_sl50_tp100 | -55% (549, 18%) | -20% (692, 8%) | -13% (4, 25%) | -18% (31, 42%) |
| sl30_tp50 | -56% (549, 20%) | -20% (692, 8%) | -22% (4, 25%) | -19% (31, 42%) |
| sl50_tp50 | -55% (549, 22%) | -20% (692, 9%) | -22% (4, 25%) | -19% (31, 42%) |
| no_stop_tp100 | -54% (549, 19%) | -20% (692, 8%) | -13% (4, 25%) | -18% (31, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20639. Outcomes:

- missed_window: 13566
- low_liquidity: 3831
- proven_liquidity_gone: 1389
- no_momentum: 743
- research_failed: 575
- simulated failed buy: 230
- proven_low_volume: 200
- proven_price_collapsed_or_parabolic: 44
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 154 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
