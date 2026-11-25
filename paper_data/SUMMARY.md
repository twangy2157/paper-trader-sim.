# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-25T03:47:56Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 12. Pools on watchlist: 37.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3735 | 12% | -65.6% | -67 to -64 | -245534 |
| all momentum | 3758 | 12% | -65.3% | -67 to -64 | -245922 |
| control | 4507 | 6% | -19.4% | -20 to -18 | -87721 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 133 | 33% | -30.1% | -38 to -21 | -4022 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3737, 12%) | -19% (4507, 6%) | -13% (47, 28%) | -30% (133, 33%) |
| wide_sl50_tp100 | -65% (3737, 13%) | -20% (4507, 6%) | -13% (47, 32%) | -31% (133, 33%) |
| sl30_tp50 | -67% (3737, 14%) | -19% (4507, 7%) | -17% (47, 34%) | -30% (133, 34%) |
| sl50_tp50 | -67% (3737, 15%) | -20% (4507, 8%) | -18% (47, 38%) | -31% (133, 34%) |
| no_stop_tp100 | -65% (3737, 14%) | -20% (4507, 7%) | -12% (47, 32%) | -32% (133, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 121791. Outcomes:

- missed_window: 78604
- low_liquidity: 20893
- proven_liquidity_gone: 10473
- no_momentum: 4556
- research_failed: 3741
- simulated failed buy: 1543
- proven_low_volume: 1542
- proven_price_collapsed_or_parabolic: 168
- proven: 134
- proven_no_uptrend: 67
- dip: 47
- research_passed: 23

Warning: 957 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
