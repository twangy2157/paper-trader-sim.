# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T23:02:58Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 33. Pools on watchlist: 2.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 547 | 16% | -53.6% | -59 to -48 | -29371 |
| all momentum | 552 | 16% | -53.5% | -59 to -48 | -29555 |
| control | 660 | 7% | -18.6% | -21 to -16 | -12310 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 30 | 43% | -17.6% | -36 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (531, 16%) | -19% (660, 7%) | -13% (4, 25%) | -18% (30, 43%) |
| wide_sl50_tp100 | -54% (531, 18%) | -19% (660, 8%) | -13% (4, 25%) | -18% (30, 43%) |
| sl30_tp50 | -55% (531, 20%) | -19% (660, 8%) | -22% (4, 25%) | -19% (30, 43%) |
| sl50_tp50 | -55% (531, 22%) | -19% (660, 9%) | -22% (4, 25%) | -19% (30, 43%) |
| no_stop_tp100 | -53% (531, 19%) | -19% (660, 8%) | -13% (4, 25%) | -18% (30, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20234. Outcomes:

- missed_window: 13345
- low_liquidity: 3747
- proven_liquidity_gone: 1337
- no_momentum: 728
- research_failed: 554
- simulated failed buy: 229
- proven_low_volume: 193
- proven_price_collapsed_or_parabolic: 40
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 152 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
