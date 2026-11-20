# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-20T19:49:41Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 18. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3289 | 11% | -66.7% | -69 to -65 | -219824 |
| all momentum | 3309 | 12% | -66.5% | -68 to -65 | -220260 |
| control | 4020 | 6% | -19.2% | -20 to -18 | -77694 |
| dip buy | 45 | 27% | -13.2% | -30 to 5 | -596 |
| proven pools | 126 | 33% | -30.7% | -39 to -21 | -3879 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3288, 12%) | -19% (4020, 6%) | -13% (45, 27%) | -31% (126, 33%) |
| wide_sl50_tp100 | -66% (3288, 13%) | -19% (4020, 7%) | -13% (45, 31%) | -32% (126, 33%) |
| sl30_tp50 | -68% (3288, 14%) | -19% (4020, 7%) | -16% (45, 33%) | -31% (126, 34%) |
| sl50_tp50 | -68% (3288, 15%) | -20% (4020, 8%) | -18% (45, 38%) | -32% (126, 34%) |
| no_stop_tp100 | -66% (3288, 14%) | -20% (4020, 7%) | -12% (45, 31%) | -32% (126, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 108788. Outcomes:

- missed_window: 70524
- low_liquidity: 18335
- proven_liquidity_gone: 9393
- no_momentum: 4069
- research_failed: 3302
- proven_low_volume: 1391
- simulated failed buy: 1363
- proven_price_collapsed_or_parabolic: 158
- proven: 126
- proven_no_uptrend: 62
- dip: 45
- research_passed: 20

Warning: 861 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
