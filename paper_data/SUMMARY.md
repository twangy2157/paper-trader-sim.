# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T12:19:10Z. Bankroll cash (research-selected trades): 684.9661609033643. Open positions: 17. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 7 | 29% | -30.4% | -72 to 15 | -215 |
| momentum, not picked | 648 | 15% | -55.3% | -60 to -51 | -35901 |
| all momentum | 655 | 15% | -55.1% | -60 to -50 | -36117 |
| control | 781 | 7% | -18.7% | -21 to -16 | -14663 |
| dip buy | 6 | 17% | -25.8% | -68 to 15 | -155 |
| proven pools | 38 | 42% | -17.9% | -34 to -2 | -681 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (634, 15%) | -19% (781, 7%) | -26% (6, 17%) | -18% (38, 42%) |
| wide_sl50_tp100 | -56% (634, 17%) | -19% (781, 8%) | -26% (6, 17%) | -18% (38, 42%) |
| sl30_tp50 | -57% (634, 19%) | -19% (781, 8%) | -31% (6, 17%) | -20% (38, 42%) |
| sl50_tp50 | -56% (634, 21%) | -19% (781, 9%) | -31% (6, 17%) | -20% (38, 42%) |
| no_stop_tp100 | -55% (634, 18%) | -19% (781, 8%) | -26% (6, 17%) | -18% (38, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 23161. Outcomes:

- missed_window: 15098
- low_liquidity: 4296
- proven_liquidity_gone: 1663
- no_momentum: 833
- research_failed: 655
- simulated failed buy: 264
- proven_low_volume: 231
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 8
- dip: 7

Warning: 172 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
