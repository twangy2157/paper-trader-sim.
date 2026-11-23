# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-23T11:40:58Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 22. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3577 | 12% | -65.8% | -68 to -64 | -235637 |
| all momentum | 3597 | 12% | -65.5% | -67 to -64 | -236074 |
| control | 4334 | 6% | -19.3% | -20 to -18 | -83880 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4017 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3576, 12%) | -19% (4334, 6%) | -13% (47, 28%) | -31% (129, 33%) |
| wide_sl50_tp100 | -65% (3576, 13%) | -20% (4334, 7%) | -13% (47, 32%) | -32% (129, 33%) |
| sl30_tp50 | -67% (3576, 14%) | -19% (4334, 7%) | -17% (47, 34%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3576, 15%) | -20% (4334, 8%) | -18% (47, 38%) | -32% (129, 33%) |
| no_stop_tp100 | -65% (3576, 14%) | -20% (4334, 7%) | -12% (47, 32%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 117661. Outcomes:

- missed_window: 76142
- low_liquidity: 20030
- proven_liquidity_gone: 10116
- no_momentum: 4390
- research_failed: 3587
- proven_low_volume: 1487
- simulated failed buy: 1484
- proven_price_collapsed_or_parabolic: 165
- proven: 129
- proven_no_uptrend: 64
- dip: 47
- research_passed: 20

Warning: 922 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
