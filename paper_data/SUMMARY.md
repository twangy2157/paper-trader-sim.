# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T10:23:20Z. Bankroll cash (research-selected trades): 751.1520680225926. Open positions: 19. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -249 |
| momentum, not picked | 637 | 15% | -55.3% | -60 to -50 | -35279 |
| all momentum | 643 | 15% | -55.2% | -60 to -50 | -35527 |
| control | 762 | 7% | -18.9% | -22 to -16 | -14468 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 36 | 42% | -16.6% | -33 to -1 | -600 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (622, 16%) | -19% (762, 7%) | -30% (5, 20%) | -17% (36, 42%) |
| wide_sl50_tp100 | -56% (622, 17%) | -19% (762, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| sl30_tp50 | -57% (622, 19%) | -19% (762, 8%) | -37% (5, 20%) | -19% (36, 42%) |
| sl50_tp50 | -57% (622, 21%) | -19% (762, 9%) | -37% (5, 20%) | -19% (36, 42%) |
| no_stop_tp100 | -55% (622, 18%) | -20% (762, 8%) | -30% (5, 20%) | -17% (36, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22699. Outcomes:

- missed_window: 14834
- low_liquidity: 4189
- proven_liquidity_gone: 1612
- no_momentum: 817
- research_failed: 642
- simulated failed buy: 260
- proven_low_volume: 227
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 6
- dip: 6

Warning: 170 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
