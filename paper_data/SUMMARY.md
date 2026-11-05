# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T09:30:54Z. Bankroll cash (research-selected trades): 751.1520680225926. Open positions: 22. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -249 |
| momentum, not picked | 629 | 15% | -55.2% | -60 to -50 | -34756 |
| all momentum | 635 | 15% | -55.0% | -60 to -50 | -35005 |
| control | 754 | 8% | -19.0% | -22 to -16 | -14416 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 36 | 42% | -16.6% | -33 to -1 | -600 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (614, 16%) | -19% (754, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| wide_sl50_tp100 | -56% (614, 17%) | -19% (754, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| sl30_tp50 | -57% (614, 19%) | -19% (754, 8%) | -37% (5, 20%) | -19% (36, 42%) |
| sl50_tp50 | -56% (614, 21%) | -20% (754, 9%) | -37% (5, 20%) | -19% (36, 42%) |
| no_stop_tp100 | -55% (614, 19%) | -20% (754, 8%) | -30% (5, 20%) | -17% (36, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22488. Outcomes:

- missed_window: 14716
- low_liquidity: 4145
- proven_liquidity_gone: 1578
- no_momentum: 810
- research_failed: 637
- simulated failed buy: 258
- proven_low_volume: 227
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 168 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
