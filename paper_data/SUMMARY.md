# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T21:17:30Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 19. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3414 | 12% | -66.2% | -68 to -64 | -226332 |
| all momentum | 3434 | 12% | -65.9% | -68 to -64 | -226768 |
| control | 4151 | 6% | -19.3% | -20 to -18 | -80584 |
| dip buy | 46 | 26% | -15.1% | -32 to 2 | -695 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4016 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3413, 12%) | -19% (4151, 6%) | -15% (46, 26%) | -31% (129, 33%) |
| wide_sl50_tp100 | -66% (3413, 13%) | -20% (4151, 6%) | -15% (46, 30%) | -32% (129, 33%) |
| sl30_tp50 | -68% (3413, 14%) | -19% (4151, 7%) | -18% (46, 33%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3413, 15%) | -20% (4151, 7%) | -19% (46, 37%) | -32% (129, 33%) |
| no_stop_tp100 | -66% (3413, 14%) | -20% (4151, 7%) | -14% (46, 30%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 112826. Outcomes:

- missed_window: 73094
- low_liquidity: 19081
- proven_liquidity_gone: 9753
- no_momentum: 4205
- research_failed: 3423
- proven_low_volume: 1431
- simulated failed buy: 1418
- proven_price_collapsed_or_parabolic: 163
- proven: 129
- proven_no_uptrend: 63
- dip: 46
- research_passed: 20

Warning: 889 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
