# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-23T11:51:31Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 19. Pools on watchlist: 35.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3580 | 12% | -65.8% | -68 to -64 | -235933 |
| all momentum | 3600 | 12% | -65.6% | -67 to -64 | -236370 |
| control | 4337 | 6% | -19.2% | -20 to -18 | -83870 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4017 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3579, 12%) | -19% (4337, 6%) | -13% (47, 28%) | -31% (129, 33%) |
| wide_sl50_tp100 | -65% (3579, 13%) | -20% (4337, 7%) | -13% (47, 32%) | -32% (129, 33%) |
| sl30_tp50 | -67% (3579, 14%) | -19% (4337, 7%) | -17% (47, 34%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3579, 15%) | -20% (4337, 8%) | -18% (47, 38%) | -32% (129, 33%) |
| no_stop_tp100 | -65% (3579, 14%) | -20% (4337, 7%) | -12% (47, 32%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 117703. Outcomes:

- missed_window: 76171
- low_liquidity: 20035
- proven_liquidity_gone: 10119
- no_momentum: 4392
- research_failed: 3588
- proven_low_volume: 1489
- simulated failed buy: 1484
- proven_price_collapsed_or_parabolic: 165
- proven: 129
- proven_no_uptrend: 64
- dip: 47
- research_passed: 20

Warning: 922 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
