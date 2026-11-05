# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T07:52:40Z. Bankroll cash (research-selected trades): 751.6520680225926. Open positions: 9. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -248 |
| momentum, not picked | 618 | 16% | -54.7% | -60 to -50 | -33831 |
| all momentum | 624 | 16% | -54.5% | -59 to -50 | -34079 |
| control | 748 | 8% | -19.0% | -22 to -16 | -14271 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 35 | 43% | -17.0% | -34 to -1 | -596 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (603, 16%) | -19% (748, 8%) | -30% (5, 20%) | -17% (35, 43%) |
| wide_sl50_tp100 | -55% (603, 18%) | -19% (748, 8%) | -30% (5, 20%) | -17% (35, 43%) |
| sl30_tp50 | -56% (603, 19%) | -19% (748, 9%) | -37% (5, 20%) | -19% (35, 43%) |
| sl50_tp50 | -56% (603, 22%) | -20% (748, 9%) | -37% (5, 20%) | -19% (35, 43%) |
| no_stop_tp100 | -54% (603, 19%) | -20% (748, 8%) | -30% (5, 20%) | -17% (35, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22046. Outcomes:

- missed_window: 14448
- low_liquidity: 4056
- proven_liquidity_gone: 1538
- no_momentum: 794
- research_failed: 623
- simulated failed buy: 246
- proven_low_volume: 225
- proven_price_collapsed_or_parabolic: 48
- proven: 37
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 164 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
