# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-25T00:51:32Z. Bankroll cash (research-selected trades): 452.209713614385. Open positions: 19. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 22 | 32% | -20.2% | -49 to 7 | -448 |
| momentum, not picked | 3705 | 12% | -65.7% | -68 to -64 | -243858 |
| all momentum | 3727 | 12% | -65.5% | -67 to -64 | -244306 |
| control | 4478 | 6% | -19.3% | -20 to -18 | -86989 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 133 | 33% | -30.1% | -38 to -21 | -4022 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3706, 12%) | -19% (4478, 6%) | -13% (47, 28%) | -30% (133, 33%) |
| wide_sl50_tp100 | -65% (3706, 13%) | -20% (4478, 6%) | -13% (47, 32%) | -31% (133, 33%) |
| sl30_tp50 | -67% (3706, 14%) | -19% (4478, 7%) | -17% (47, 34%) | -30% (133, 34%) |
| sl50_tp50 | -67% (3706, 15%) | -20% (4478, 8%) | -18% (47, 38%) | -31% (133, 34%) |
| no_stop_tp100 | -65% (3706, 14%) | -20% (4478, 7%) | -12% (47, 32%) | -32% (133, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 121133. Outcomes:

- missed_window: 78205
- low_liquidity: 20788
- proven_liquidity_gone: 10390
- no_momentum: 4532
- research_failed: 3713
- simulated failed buy: 1535
- proven_low_volume: 1535
- proven_price_collapsed_or_parabolic: 167
- proven: 133
- proven_no_uptrend: 65
- dip: 47
- research_passed: 23

Warning: 952 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
