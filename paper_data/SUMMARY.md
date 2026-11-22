# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-22T22:16:11Z. Bankroll cash (research-selected trades): 563.74568815387. Open positions: 13. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 20 | 35% | -21.7% | -51 to 10 | -436 |
| momentum, not picked | 3514 | 12% | -66.0% | -68 to -64 | -232258 |
| all momentum | 3534 | 12% | -65.8% | -68 to -64 | -232694 |
| control | 4253 | 6% | -19.3% | -20 to -18 | -82475 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 129 | 33% | -31.0% | -40 to -22 | -4017 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3513, 12%) | -19% (4253, 6%) | -13% (47, 28%) | -31% (129, 33%) |
| wide_sl50_tp100 | -66% (3513, 13%) | -20% (4253, 6%) | -13% (47, 32%) | -32% (129, 33%) |
| sl30_tp50 | -67% (3513, 14%) | -19% (4253, 7%) | -17% (47, 34%) | -31% (129, 33%) |
| sl50_tp50 | -67% (3513, 15%) | -20% (4253, 8%) | -18% (47, 38%) | -32% (129, 33%) |
| no_stop_tp100 | -65% (3513, 14%) | -20% (4253, 7%) | -12% (47, 32%) | -33% (129, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 115927. Outcomes:

- missed_window: 75093
- low_liquidity: 19688
- proven_liquidity_gone: 9968
- no_momentum: 4305
- research_failed: 3519
- proven_low_volume: 1470
- simulated failed buy: 1461
- proven_price_collapsed_or_parabolic: 163
- proven: 129
- proven_no_uptrend: 64
- dip: 47
- research_passed: 20

Warning: 905 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
