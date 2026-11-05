# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T10:54:53Z. Bankroll cash (research-selected trades): 751.1520680225926. Open positions: 15. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 6 | 17% | -41.1% | -82 to 7 | -249 |
| momentum, not picked | 639 | 15% | -55.1% | -60 to -50 | -35287 |
| all momentum | 645 | 15% | -55.0% | -60 to -50 | -35536 |
| control | 769 | 7% | -18.9% | -22 to -16 | -14621 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 37 | 41% | -18.9% | -36 to -2 | -701 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (624, 16%) | -19% (769, 7%) | -30% (5, 20%) | -19% (37, 41%) |
| wide_sl50_tp100 | -56% (624, 17%) | -19% (769, 8%) | -30% (5, 20%) | -19% (37, 41%) |
| sl30_tp50 | -57% (624, 19%) | -19% (769, 8%) | -37% (5, 20%) | -21% (37, 41%) |
| sl50_tp50 | -56% (624, 21%) | -19% (769, 9%) | -37% (5, 20%) | -21% (37, 41%) |
| no_stop_tp100 | -55% (624, 18%) | -20% (769, 8%) | -30% (5, 20%) | -19% (37, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 22843. Outcomes:

- missed_window: 14924
- low_liquidity: 4224
- proven_liquidity_gone: 1625
- no_momentum: 821
- research_failed: 644
- simulated failed buy: 260
- proven_low_volume: 227
- proven_price_collapsed_or_parabolic: 48
- proven: 38
- proven_no_uptrend: 20
- research_passed: 6
- dip: 6

Warning: 170 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
