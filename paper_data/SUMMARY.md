# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T09:41:10Z. Bankroll cash (research-selected trades): 751.1520680225926. Open positions: 20. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -249 |
| momentum, not picked | 630 | 15% | -55.2% | -60 to -50 | -34856 |
| all momentum | 636 | 15% | -55.1% | -60 to -50 | -35105 |
| control | 757 | 8% | -19.0% | -22 to -16 | -14432 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 36 | 42% | -16.6% | -33 to -1 | -600 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (615, 16%) | -19% (757, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| wide_sl50_tp100 | -56% (615, 17%) | -19% (757, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| sl30_tp50 | -57% (615, 19%) | -19% (757, 8%) | -37% (5, 20%) | -19% (36, 42%) |
| sl50_tp50 | -56% (615, 21%) | -19% (757, 9%) | -37% (5, 20%) | -19% (36, 42%) |
| no_stop_tp100 | -55% (615, 19%) | -20% (757, 8%) | -30% (5, 20%) | -17% (36, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22529. Outcomes:

- missed_window: 14738
- low_liquidity: 4155
- proven_liquidity_gone: 1584
- no_momentum: 812
- research_failed: 637
- simulated failed buy: 259
- proven_low_volume: 227
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 169 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
