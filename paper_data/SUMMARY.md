# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T17:29:21Z. Bankroll cash (research-selected trades): 913.731903378573. Open positions: 40. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 4 | 25% | -21.2% | - | -86 |
| momentum, not picked | 504 | 15% | -53.5% | -59 to -48 | -26984 |
| all momentum | 508 | 16% | -53.2% | -59 to -48 | -27070 |
| control | 604 | 7% | -18.8% | -22 to -16 | -11443 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 28 | 39% | -18.9% | -38 to -1 | -532 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (487, 16%) | -19% (604, 7%) | -13% (4, 25%) | -19% (28, 39%) |
| wide_sl50_tp100 | -54% (487, 18%) | -19% (604, 7%) | -13% (4, 25%) | -19% (28, 39%) |
| sl30_tp50 | -56% (487, 19%) | -19% (604, 8%) | -22% (4, 25%) | -21% (28, 39%) |
| sl50_tp50 | -55% (487, 22%) | -19% (604, 9%) | -22% (4, 25%) | -21% (28, 39%) |
| no_stop_tp100 | -53% (487, 19%) | -20% (604, 7%) | -13% (4, 25%) | -19% (28, 39%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18825. Outcomes:

- missed_window: 12453
- low_liquidity: 3494
- proven_liquidity_gone: 1209
- no_momentum: 671
- research_failed: 520
- simulated failed buy: 214
- proven_low_volume: 175
- proven_price_collapsed_or_parabolic: 36
- proven: 29
- proven_no_uptrend: 16
- research_passed: 4
- dip: 4

Warning: 145 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
