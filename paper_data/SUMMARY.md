# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T19:10:52Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 10. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3398 | 12% | -66.2% | -68 to -64 | -225173 |
| all momentum | 3418 | 12% | -65.9% | -68 to -64 | -225610 |
| control | 4133 | 6% | -19.3% | -20 to -18 | -80059 |
| dip buy | 46 | 26% | -15.1% | -32 to 2 | -695 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4016 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3397, 12%) | -19% (4133, 6%) | -15% (46, 26%) | -31% (129, 33%) |
| wide_sl50_tp100 | -66% (3397, 13%) | -20% (4133, 6%) | -15% (46, 30%) | -32% (129, 33%) |
| sl30_tp50 | -68% (3397, 14%) | -19% (4133, 7%) | -18% (46, 33%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3397, 15%) | -20% (4133, 7%) | -19% (46, 37%) | -32% (129, 33%) |
| no_stop_tp100 | -66% (3397, 14%) | -20% (4133, 7%) | -14% (46, 30%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 112232. Outcomes:

- missed_window: 72710
- low_liquidity: 18938
- proven_liquidity_gone: 9743
- no_momentum: 4181
- research_failed: 3404
- proven_low_volume: 1430
- simulated failed buy: 1405
- proven_price_collapsed_or_parabolic: 163
- proven: 129
- proven_no_uptrend: 63
- dip: 46
- research_passed: 20

Warning: 883 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
