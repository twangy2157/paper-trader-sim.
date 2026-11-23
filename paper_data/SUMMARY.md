# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-23T12:12:39Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 14. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3583 | 12% | -65.8% | -68 to -64 | -236233 |
| all momentum | 3603 | 12% | -65.6% | -67 to -64 | -236669 |
| control | 4343 | 6% | -19.2% | -20 to -18 | -83907 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4017 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3582, 12%) | -19% (4343, 6%) | -13% (47, 28%) | -31% (129, 33%) |
| wide_sl50_tp100 | -65% (3582, 13%) | -20% (4343, 7%) | -13% (47, 32%) | -32% (129, 33%) |
| sl30_tp50 | -67% (3582, 14%) | -19% (4343, 7%) | -17% (47, 34%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3582, 15%) | -20% (4343, 8%) | -18% (47, 38%) | -32% (129, 33%) |
| no_stop_tp100 | -65% (3582, 14%) | -20% (4343, 7%) | -12% (47, 32%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 117776. Outcomes:

- missed_window: 76215
- low_liquidity: 20045
- proven_liquidity_gone: 10131
- no_momentum: 4393
- research_failed: 3591
- proven_low_volume: 1491
- simulated failed buy: 1485
- proven_price_collapsed_or_parabolic: 165
- proven: 129
- proven_no_uptrend: 64
- dip: 47
- research_passed: 20

Warning: 924 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
