# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T05:34:08Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 15. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3345 | 12% | -66.4% | -68 to -64 | -222369 |
| all momentum | 3365 | 12% | -66.1% | -68 to -64 | -222806 |
| control | 4082 | 6% | -19.2% | -20 to -18 | -78848 |
| dip buy | 46 | 26% | -15.1% | -32 to 2 | -695 |
| proven pools | 126 | 33% | -30.7% | -39 to -21 | -3879 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3344, 12%) | -19% (4082, 6%) | -15% (46, 26%) | -31% (126, 33%) |
| wide_sl50_tp100 | -66% (3344, 13%) | -19% (4082, 6%) | -15% (46, 30%) | -32% (126, 33%) |
| sl30_tp50 | -68% (3344, 14%) | -19% (4082, 7%) | -18% (46, 33%) | -31% (126, 34%) |
| sl50_tp50 | -67% (3344, 15%) | -20% (4082, 8%) | -19% (46, 37%) | -32% (126, 34%) |
| no_stop_tp100 | -66% (3344, 14%) | -20% (4082, 7%) | -14% (46, 30%) | -32% (126, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 110645. Outcomes:

- missed_window: 71693
- low_liquidity: 18666
- proven_liquidity_gone: 9587
- no_momentum: 4134
- research_failed: 3351
- proven_low_volume: 1412
- simulated failed buy: 1387
- proven_price_collapsed_or_parabolic: 160
- proven: 127
- proven_no_uptrend: 62
- dip: 46
- research_passed: 20

Warning: 875 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
