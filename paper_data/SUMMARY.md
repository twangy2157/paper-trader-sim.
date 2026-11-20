# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T18:14:11Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 20. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3273 | 11% | -66.9% | -69 to -65 | -219416 |
| all momentum | 3293 | 12% | -66.7% | -69 to -65 | -219852 |
| control | 4006 | 6% | -19.2% | -20 to -18 | -77274 |
| dip buy | 45 | 27% | -13.2% | -30 to 5 | -596 |
| proven pools | 126 | 33% | -30.7% | -39 to -21 | -3879 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3272, 12%) | -19% (4006, 6%) | -13% (45, 27%) | -31% (126, 33%) |
| wide_sl50_tp100 | -67% (3272, 13%) | -19% (4006, 7%) | -13% (45, 31%) | -32% (126, 33%) |
| sl30_tp50 | -68% (3272, 14%) | -19% (4006, 7%) | -16% (45, 33%) | -31% (126, 34%) |
| sl50_tp50 | -68% (3272, 15%) | -20% (4006, 8%) | -18% (45, 38%) | -32% (126, 34%) |
| no_stop_tp100 | -66% (3272, 14%) | -20% (4006, 7%) | -12% (45, 31%) | -32% (126, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 108446. Outcomes:

- missed_window: 70340
- low_liquidity: 18247
- proven_liquidity_gone: 9358
- no_momentum: 4060
- research_failed: 3283
- proven_low_volume: 1385
- simulated failed buy: 1362
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 45
- research_passed: 20

Warning: 860 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
