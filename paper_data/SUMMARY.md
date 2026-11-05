# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T09:20:45Z. Bankroll cash (research-selected trades): 751.6520680225926. Open positions: 21. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -248 |
| momentum, not picked | 628 | 15% | -55.1% | -60 to -50 | -34656 |
| all momentum | 634 | 15% | -55.0% | -60 to -50 | -34905 |
| control | 752 | 8% | -18.9% | -22 to -16 | -14311 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 36 | 42% | -16.6% | -33 to -1 | -600 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (613, 16%) | -19% (752, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| wide_sl50_tp100 | -56% (613, 17%) | -19% (752, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| sl30_tp50 | -57% (613, 19%) | -19% (752, 9%) | -37% (5, 20%) | -19% (36, 42%) |
| sl50_tp50 | -56% (613, 21%) | -19% (752, 9%) | -37% (5, 20%) | -19% (36, 42%) |
| no_stop_tp100 | -55% (613, 19%) | -20% (752, 8%) | -30% (5, 20%) | -17% (36, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22433. Outcomes:

- missed_window: 14677
- low_liquidity: 4140
- proven_liquidity_gone: 1573
- no_momentum: 806
- research_failed: 637
- simulated failed buy: 257
- proven_low_volume: 226
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 168 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
