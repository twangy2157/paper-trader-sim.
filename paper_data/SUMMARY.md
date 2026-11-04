# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T22:52:17Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 26. Pools on watchlist: 25.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 546 | 15% | -53.8% | -59 to -48 | -29407 |
| all momentum | 551 | 15% | -53.6% | -59 to -48 | -29590 |
| control | 659 | 7% | -18.6% | -22 to -16 | -12298 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 30 | 43% | -17.6% | -36 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (530, 16%) | -19% (659, 7%) | -13% (4, 25%) | -18% (30, 43%) |
| wide_sl50_tp100 | -54% (530, 18%) | -19% (659, 8%) | -13% (4, 25%) | -18% (30, 43%) |
| sl30_tp50 | -55% (530, 20%) | -19% (659, 8%) | -22% (4, 25%) | -19% (30, 43%) |
| sl50_tp50 | -55% (530, 22%) | -19% (659, 9%) | -22% (4, 25%) | -19% (30, 43%) |
| no_stop_tp100 | -53% (530, 19%) | -19% (659, 8%) | -13% (4, 25%) | -18% (30, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20202. Outcomes:

- missed_window: 13333
- low_liquidity: 3743
- proven_liquidity_gone: 1331
- no_momentum: 722
- research_failed: 552
- simulated failed buy: 228
- proven_low_volume: 193
- proven_price_collapsed_or_parabolic: 40
- proven: 31
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 151 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
