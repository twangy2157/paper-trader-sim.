# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T18:00:10Z. Bankroll cash (research-selected trades): 913.731903378573. Open positions: 27. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 4 | 25% | -21.2% | - | -86 |
| momentum, not picked | 510 | 15% | -53.4% | -59 to -48 | -27278 |
| all momentum | 514 | 16% | -53.2% | -58 to -47 | -27364 |
| control | 613 | 7% | -19.0% | -22 to -16 | -11727 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 29 | 41% | -18.2% | -37 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (493, 16%) | -19% (613, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| wide_sl50_tp100 | -54% (493, 18%) | -20% (613, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| sl30_tp50 | -55% (493, 20%) | -19% (613, 8%) | -22% (4, 25%) | -20% (29, 41%) |
| sl50_tp50 | -55% (493, 22%) | -19% (613, 9%) | -22% (4, 25%) | -20% (29, 41%) |
| no_stop_tp100 | -53% (493, 19%) | -20% (613, 7%) | -13% (4, 25%) | -18% (29, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18987. Outcomes:

- missed_window: 12574
- low_liquidity: 3512
- proven_liquidity_gone: 1223
- no_momentum: 673
- research_failed: 521
- simulated failed buy: 214
- proven_low_volume: 177
- proven_price_collapsed_or_parabolic: 37
- proven: 29
- proven_no_uptrend: 19
- research_passed: 4
- dip: 4

Warning: 145 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
