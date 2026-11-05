# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T09:09:29Z. Bankroll cash (research-selected trades): 751.6520680225926. Open positions: 21. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -248 |
| momentum, not picked | 626 | 15% | -55.0% | -60 to -50 | -34477 |
| all momentum | 632 | 15% | -54.9% | -60 to -50 | -34725 |
| control | 751 | 8% | -18.9% | -22 to -16 | -14298 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 36 | 42% | -16.6% | -33 to -1 | -600 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (611, 16%) | -19% (751, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| wide_sl50_tp100 | -55% (611, 18%) | -19% (751, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| sl30_tp50 | -57% (611, 19%) | -19% (751, 9%) | -37% (5, 20%) | -19% (36, 42%) |
| sl50_tp50 | -56% (611, 21%) | -19% (751, 9%) | -37% (5, 20%) | -19% (36, 42%) |
| no_stop_tp100 | -55% (611, 19%) | -20% (751, 8%) | -30% (5, 20%) | -17% (36, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22384. Outcomes:

- missed_window: 14648
- low_liquidity: 4129
- proven_liquidity_gone: 1568
- no_momentum: 803
- research_failed: 637
- simulated failed buy: 256
- proven_low_volume: 226
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 167 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
