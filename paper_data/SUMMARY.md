# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T15:53:43Z. Bankroll cash (research-selected trades): 759.5946161788225. Open positions: 18. Pools on watchlist: 82.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 496 | 15% | -54.4% | -60 to -49 | -27014 |
| all momentum | 498 | 15% | -54.4% | -60 to -49 | -27154 |
| control | 594 | 7% | -18.4% | -21 to -15 | -10999 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 27 | 41% | -15.9% | -35 to 2 | -431 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (477, 15%) | -18% (594, 7%) | -13% (4, 25%) | -16% (27, 41%) |
| wide_sl50_tp100 | -55% (477, 17%) | -19% (594, 8%) | -13% (4, 25%) | -16% (27, 41%) |
| sl30_tp50 | -57% (477, 19%) | -19% (594, 8%) | -22% (4, 25%) | -18% (27, 41%) |
| sl50_tp50 | -56% (477, 21%) | -19% (594, 9%) | -22% (4, 25%) | -18% (27, 41%) |
| no_stop_tp100 | -54% (477, 18%) | -19% (594, 8%) | -13% (4, 25%) | -16% (27, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18351. Outcomes:

- missed_window: 12143
- low_liquidity: 3419
- proven_liquidity_gone: 1172
- no_momentum: 647
- research_failed: 502
- simulated failed buy: 209
- proven_low_volume: 174
- proven_price_collapsed_or_parabolic: 34
- proven: 29
- proven_no_uptrend: 15
- dip: 4
- research_passed: 3

Warning: 139 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
