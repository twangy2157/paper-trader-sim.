# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T17:21:36Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 15. Pools on watchlist: 70.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3267 | 11% | -67.1% | -69 to -65 | -219441 |
| all momentum | 3287 | 11% | -66.8% | -69 to -65 | -219877 |
| control | 3999 | 6% | -19.2% | -20 to -18 | -77035 |
| dip buy | 45 | 27% | -13.2% | -30 to 5 | -596 |
| proven pools | 126 | 33% | -30.7% | -39 to -21 | -3879 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3266, 11%) | -19% (3999, 6%) | -13% (45, 27%) | -31% (126, 33%) |
| wide_sl50_tp100 | -67% (3266, 13%) | -19% (3999, 7%) | -13% (45, 31%) | -32% (126, 33%) |
| sl30_tp50 | -68% (3266, 14%) | -19% (3999, 7%) | -16% (45, 33%) | -31% (126, 34%) |
| sl50_tp50 | -68% (3266, 15%) | -20% (3999, 8%) | -18% (45, 38%) | -32% (126, 34%) |
| no_stop_tp100 | -67% (3266, 13%) | -20% (3999, 7%) | -12% (45, 31%) | -32% (126, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 108225. Outcomes:

- missed_window: 70216
- low_liquidity: 18205
- proven_liquidity_gone: 9325
- no_momentum: 4050
- research_failed: 3275
- proven_low_volume: 1383
- simulated failed buy: 1360
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 45
- research_passed: 20

Warning: 857 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
