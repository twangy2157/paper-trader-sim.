# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T09:51:32Z. Bankroll cash (research-selected trades): 751.1520680225926. Open positions: 19. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -249 |
| momentum, not picked | 632 | 15% | -55.4% | -60 to -50 | -35056 |
| all momentum | 638 | 15% | -55.2% | -60 to -51 | -35305 |
| control | 758 | 8% | -19.0% | -22 to -16 | -14436 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 36 | 42% | -16.6% | -33 to -1 | -600 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (617, 16%) | -19% (758, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| wide_sl50_tp100 | -56% (617, 17%) | -19% (758, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| sl30_tp50 | -57% (617, 19%) | -19% (758, 8%) | -37% (5, 20%) | -19% (36, 42%) |
| sl50_tp50 | -57% (617, 21%) | -19% (758, 9%) | -37% (5, 20%) | -19% (36, 42%) |
| no_stop_tp100 | -55% (617, 18%) | -20% (758, 8%) | -30% (5, 20%) | -17% (36, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22570. Outcomes:

- missed_window: 14760
- low_liquidity: 4165
- proven_liquidity_gone: 1591
- no_momentum: 813
- research_failed: 638
- simulated failed buy: 259
- proven_low_volume: 227
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 169 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
