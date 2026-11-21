# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-21T04:38:33Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 18. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3339 | 12% | -66.5% | -68 to -65 | -222423 |
| all momentum | 3359 | 12% | -66.3% | -68 to -64 | -222859 |
| control | 4072 | 6% | -19.2% | -20 to -18 | -78407 |
| dip buy | 45 | 27% | -13.2% | -30 to 5 | -596 |
| proven pools | 126 | 33% | -30.7% | -39 to -21 | -3879 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3338, 12%) | -19% (4072, 6%) | -13% (45, 27%) | -31% (126, 33%) |
| wide_sl50_tp100 | -66% (3338, 13%) | -19% (4072, 6%) | -13% (45, 31%) | -32% (126, 33%) |
| sl30_tp50 | -68% (3338, 14%) | -19% (4072, 7%) | -16% (45, 33%) | -31% (126, 34%) |
| sl50_tp50 | -68% (3338, 15%) | -19% (4072, 8%) | -18% (45, 38%) | -32% (126, 34%) |
| no_stop_tp100 | -66% (3338, 14%) | -20% (4072, 7%) | -12% (45, 31%) | -32% (126, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 110411. Outcomes:

- missed_window: 71549
- low_liquidity: 18629
- proven_liquidity_gone: 9555
- no_momentum: 4126
- research_failed: 3345
- proven_low_volume: 1410
- simulated failed buy: 1383
- proven_price_collapsed_or_parabolic: 159
- proven: 127
- proven_no_uptrend: 62
- dip: 46
- research_passed: 20

Warning: 875 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
