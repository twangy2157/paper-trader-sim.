# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T21:37:11Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 20. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 533 | 16% | -53.3% | -59 to -47 | -28448 |
| all momentum | 538 | 16% | -53.1% | -58 to -48 | -28632 |
| control | 649 | 7% | -18.7% | -22 to -16 | -12211 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 30 | 43% | -17.6% | -36 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (517, 16%) | -19% (649, 7%) | -13% (4, 25%) | -18% (30, 43%) |
| wide_sl50_tp100 | -53% (517, 18%) | -19% (649, 8%) | -13% (4, 25%) | -18% (30, 43%) |
| sl30_tp50 | -55% (517, 20%) | -19% (649, 8%) | -22% (4, 25%) | -19% (30, 43%) |
| sl50_tp50 | -54% (517, 23%) | -19% (649, 9%) | -22% (4, 25%) | -19% (30, 43%) |
| no_stop_tp100 | -53% (517, 19%) | -19% (649, 8%) | -13% (4, 25%) | -18% (30, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 19861. Outcomes:

- missed_window: 13118
- low_liquidity: 3679
- proven_liquidity_gone: 1304
- no_momentum: 701
- research_failed: 544
- simulated failed buy: 224
- proven_low_volume: 191
- proven_price_collapsed_or_parabolic: 40
- proven: 31
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 151 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
