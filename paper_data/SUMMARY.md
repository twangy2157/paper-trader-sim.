# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T10:01:41Z. Bankroll cash (research-selected trades): 751.1520680225926. Open positions: 19. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -249 |
| momentum, not picked | 635 | 15% | -55.3% | -60 to -50 | -35172 |
| all momentum | 641 | 15% | -55.2% | -60 to -50 | -35421 |
| control | 758 | 8% | -19.0% | -22 to -16 | -14436 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 36 | 42% | -16.6% | -33 to -1 | -600 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (620, 16%) | -19% (758, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| wide_sl50_tp100 | -56% (620, 17%) | -19% (758, 8%) | -30% (5, 20%) | -17% (36, 42%) |
| sl30_tp50 | -57% (620, 19%) | -19% (758, 8%) | -37% (5, 20%) | -19% (36, 42%) |
| sl50_tp50 | -57% (620, 21%) | -19% (758, 9%) | -37% (5, 20%) | -19% (36, 42%) |
| no_stop_tp100 | -55% (620, 19%) | -20% (758, 8%) | -30% (5, 20%) | -17% (36, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22621. Outcomes:

- missed_window: 14793
- low_liquidity: 4173
- proven_liquidity_gone: 1598
- no_momentum: 814
- research_failed: 640
- simulated failed buy: 259
- proven_low_volume: 227
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 169 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
