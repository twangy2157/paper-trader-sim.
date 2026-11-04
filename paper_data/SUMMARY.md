# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T22:42:08Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 24. Pools on watchlist: 25.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 545 | 15% | -53.7% | -59 to -48 | -29306 |
| all momentum | 550 | 15% | -53.5% | -58 to -48 | -29489 |
| control | 657 | 7% | -18.7% | -22 to -16 | -12373 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 30 | 43% | -17.6% | -36 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (529, 16%) | -19% (657, 7%) | -13% (4, 25%) | -18% (30, 43%) |
| wide_sl50_tp100 | -54% (529, 18%) | -19% (657, 8%) | -13% (4, 25%) | -18% (30, 43%) |
| sl30_tp50 | -55% (529, 20%) | -19% (657, 8%) | -22% (4, 25%) | -19% (30, 43%) |
| sl50_tp50 | -55% (529, 22%) | -19% (657, 9%) | -22% (4, 25%) | -19% (30, 43%) |
| no_stop_tp100 | -53% (529, 19%) | -19% (657, 8%) | -13% (4, 25%) | -18% (30, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20174. Outcomes:

- missed_window: 13320
- low_liquidity: 3735
- proven_liquidity_gone: 1331
- no_momentum: 718
- research_failed: 551
- simulated failed buy: 226
- proven_low_volume: 193
- proven_price_collapsed_or_parabolic: 40
- proven: 31
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 151 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
