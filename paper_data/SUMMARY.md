# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T07:19:30Z. Bankroll cash (research-selected trades): 716.8065461812329. Open positions: 17. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 610 | 16% | -54.5% | -59 to -49 | -33286 |
| all momentum | 615 | 16% | -54.3% | -59 to -49 | -33469 |
| control | 744 | 8% | -18.9% | -22 to -16 | -14126 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 34 | 44% | -17.5% | -34 to -2 | -596 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (594, 16%) | -19% (744, 8%) | -13% (4, 25%) | -17% (34, 44%) |
| wide_sl50_tp100 | -55% (594, 18%) | -19% (744, 8%) | -13% (4, 25%) | -17% (34, 44%) |
| sl30_tp50 | -56% (594, 19%) | -19% (744, 8%) | -22% (4, 25%) | -20% (34, 44%) |
| sl50_tp50 | -56% (594, 22%) | -20% (744, 9%) | -22% (4, 25%) | -20% (34, 44%) |
| no_stop_tp100 | -54% (594, 19%) | -20% (744, 8%) | -13% (4, 25%) | -17% (34, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21901. Outcomes:

- missed_window: 14349
- low_liquidity: 4038
- proven_liquidity_gone: 1519
- no_momentum: 792
- research_failed: 619
- simulated failed buy: 245
- proven_low_volume: 224
- proven_price_collapsed_or_parabolic: 48
- proven: 36
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 164 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
