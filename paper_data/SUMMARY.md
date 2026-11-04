# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T18:20:42Z. Bankroll cash (research-selected trades): 913.731903378573. Open positions: 16. Pools on watchlist: 28.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 4 | 25% | -21.2% | - | -86 |
| momentum, not picked | 516 | 16% | -52.9% | -59 to -47 | -27365 |
| all momentum | 520 | 16% | -52.7% | -58 to -47 | -27452 |
| control | 621 | 7% | -19.2% | -22 to -16 | -11979 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 29 | 41% | -18.2% | -37 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (499, 16%) | -19% (621, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| wide_sl50_tp100 | -53% (499, 18%) | -20% (621, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| sl30_tp50 | -55% (499, 20%) | -19% (621, 8%) | -22% (4, 25%) | -20% (29, 41%) |
| sl50_tp50 | -54% (499, 23%) | -19% (621, 9%) | -22% (4, 25%) | -20% (29, 41%) |
| no_stop_tp100 | -52% (499, 19%) | -20% (621, 7%) | -13% (4, 25%) | -18% (29, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 19093. Outcomes:

- missed_window: 12658
- low_liquidity: 3518
- proven_liquidity_gone: 1234
- no_momentum: 675
- research_failed: 521
- simulated failed buy: 215
- proven_low_volume: 177
- proven_price_collapsed_or_parabolic: 38
- proven: 30
- proven_no_uptrend: 19
- research_passed: 4
- dip: 4

Warning: 145 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
