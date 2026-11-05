# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T07:29:39Z. Bankroll cash (research-selected trades): 716.8065461812329. Open positions: 12. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 614 | 15% | -54.8% | -60 to -50 | -33686 |
| all momentum | 619 | 16% | -54.6% | -60 to -50 | -33869 |
| control | 746 | 8% | -19.0% | -22 to -16 | -14232 |
| dip buy | 5 | 20% | -30.5% | - | -152 |
| proven pools | 34 | 44% | -17.5% | -34 to -2 | -596 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (598, 16%) | -19% (746, 8%) | -30% (5, 20%) | -17% (34, 44%) |
| wide_sl50_tp100 | -55% (598, 18%) | -19% (746, 8%) | -30% (5, 20%) | -17% (34, 44%) |
| sl30_tp50 | -57% (598, 19%) | -19% (746, 9%) | -37% (5, 20%) | -20% (34, 44%) |
| sl50_tp50 | -56% (598, 21%) | -19% (746, 9%) | -37% (5, 20%) | -20% (34, 44%) |
| no_stop_tp100 | -54% (598, 19%) | -20% (746, 8%) | -30% (5, 20%) | -17% (34, 44%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21941. Outcomes:

- missed_window: 14379
- low_liquidity: 4041
- proven_liquidity_gone: 1524
- no_momentum: 792
- research_failed: 620
- simulated failed buy: 245
- proven_low_volume: 224
- proven_price_collapsed_or_parabolic: 48
- proven: 37
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 164 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
