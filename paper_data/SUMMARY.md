# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-25T01:54:10Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 16. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3713 | 12% | -65.6% | -68 to -64 | -244080 |
| all momentum | 3736 | 12% | -65.3% | -67 to -63 | -244468 |
| control | 4488 | 6% | -19.4% | -20 to -18 | -87260 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 133 | 33% | -30.1% | -38 to -21 | -4022 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3715, 12%) | -19% (4488, 6%) | -13% (47, 28%) | -30% (133, 33%) |
| wide_sl50_tp100 | -65% (3715, 13%) | -20% (4488, 6%) | -13% (47, 32%) | -31% (133, 33%) |
| sl30_tp50 | -67% (3715, 14%) | -19% (4488, 7%) | -17% (47, 34%) | -30% (133, 34%) |
| sl50_tp50 | -67% (3715, 15%) | -20% (4488, 8%) | -18% (47, 38%) | -31% (133, 34%) |
| no_stop_tp100 | -65% (3715, 14%) | -20% (4488, 7%) | -12% (47, 32%) | -32% (133, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 121375. Outcomes:

- missed_window: 78350
- low_liquidity: 20832
- proven_liquidity_gone: 10421
- no_momentum: 4543
- research_failed: 3718
- simulated failed buy: 1538
- proven_low_volume: 1538
- proven_price_collapsed_or_parabolic: 167
- proven: 133
- proven_no_uptrend: 65
- dip: 47
- research_passed: 23

Warning: 954 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
