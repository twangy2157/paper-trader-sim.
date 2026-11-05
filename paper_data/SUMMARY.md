# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-05T06:34:56Z. Bankroll cash (research-selected trades): 716.8065461812329. Open positions: 24. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 606 | 16% | -54.3% | -59 to -49 | -32975 |
| all momentum | 611 | 16% | -54.2% | -59 to -49 | -33158 |
| control | 741 | 8% | -18.8% | -21 to -16 | -14010 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 33 | 42% | -19.4% | -36 to -3 | -642 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (590, 16%) | -19% (741, 8%) | -13% (4, 25%) | -19% (33, 42%) |
| wide_sl50_tp100 | -55% (590, 18%) | -19% (741, 8%) | -13% (4, 25%) | -19% (33, 42%) |
| sl30_tp50 | -56% (590, 19%) | -19% (741, 9%) | -22% (4, 25%) | -21% (33, 42%) |
| sl50_tp50 | -56% (590, 22%) | -19% (741, 9%) | -22% (4, 25%) | -21% (33, 42%) |
| no_stop_tp100 | -54% (590, 19%) | -19% (741, 8%) | -13% (4, 25%) | -19% (33, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 21850. Outcomes:

- missed_window: 14306
- low_liquidity: 4038
- proven_liquidity_gone: 1513
- no_momentum: 792
- research_failed: 618
- simulated failed buy: 245
- proven_low_volume: 223
- proven_price_collapsed_or_parabolic: 48
- proven: 36
- proven_no_uptrend: 20
- research_passed: 6
- dip: 5

Warning: 163 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
