# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-22T08:13:54Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 18. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3460 | 12% | -66.2% | -68 to -64 | -229311 |
| all momentum | 3480 | 12% | -65.9% | -68 to -64 | -229748 |
| control | 4194 | 6% | -19.3% | -20 to -18 | -81321 |
| dip buy | 46 | 26% | -15.1% | -32 to 2 | -695 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4017 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3459, 12%) | -19% (4194, 6%) | -15% (46, 26%) | -31% (129, 33%) |
| wide_sl50_tp100 | -66% (3459, 13%) | -20% (4194, 6%) | -15% (46, 30%) | -32% (129, 33%) |
| sl30_tp50 | -68% (3459, 14%) | -19% (4194, 7%) | -18% (46, 33%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3459, 15%) | -20% (4194, 7%) | -19% (46, 37%) | -32% (129, 33%) |
| no_stop_tp100 | -66% (3459, 14%) | -20% (4194, 7%) | -14% (46, 30%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 114210. Outcomes:

- missed_window: 73978
- low_liquidity: 19360
- proven_liquidity_gone: 9842
- no_momentum: 4249
- research_failed: 3466
- proven_low_volume: 1447
- simulated failed buy: 1445
- proven_price_collapsed_or_parabolic: 163
- proven: 129
- proven_no_uptrend: 64
- dip: 47
- research_passed: 20

Warning: 896 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
