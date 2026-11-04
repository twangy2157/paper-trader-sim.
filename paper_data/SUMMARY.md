# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T21:48:40Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 19. Pools on watchlist: 103.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 535 | 16% | -53.3% | -59 to -48 | -28559 |
| all momentum | 540 | 16% | -53.1% | -58 to -48 | -28742 |
| control | 651 | 7% | -18.7% | -22 to -16 | -12221 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 30 | 43% | -17.6% | -36 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (519, 16%) | -19% (651, 7%) | -13% (4, 25%) | -18% (30, 43%) |
| wide_sl50_tp100 | -53% (519, 18%) | -19% (651, 8%) | -13% (4, 25%) | -18% (30, 43%) |
| sl30_tp50 | -55% (519, 20%) | -19% (651, 8%) | -22% (4, 25%) | -19% (30, 43%) |
| sl50_tp50 | -54% (519, 23%) | -19% (651, 9%) | -22% (4, 25%) | -19% (30, 43%) |
| no_stop_tp100 | -53% (519, 19%) | -19% (651, 8%) | -13% (4, 25%) | -18% (30, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 19912. Outcomes:

- missed_window: 13151
- low_liquidity: 3687
- proven_liquidity_gone: 1311
- no_momentum: 703
- research_failed: 545
- simulated failed buy: 224
- proven_low_volume: 191
- proven_price_collapsed_or_parabolic: 40
- proven: 31
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 151 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
