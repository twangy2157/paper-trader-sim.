# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T18:31:02Z. Bankroll cash (research-selected trades): 913.731903378573. Open positions: 9. Pools on watchlist: 0.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 4 | 25% | -21.2% | - | -86 |
| momentum, not picked | 518 | 15% | -52.9% | -59 to -48 | -27469 |
| all momentum | 522 | 16% | -52.7% | -58 to -47 | -27556 |
| control | 626 | 7% | -18.9% | -22 to -16 | -11913 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 29 | 41% | -18.2% | -37 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (501, 16%) | -19% (626, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| wide_sl50_tp100 | -53% (501, 18%) | -19% (626, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| sl30_tp50 | -55% (501, 20%) | -19% (626, 8%) | -22% (4, 25%) | -20% (29, 41%) |
| sl50_tp50 | -54% (501, 23%) | -19% (626, 9%) | -22% (4, 25%) | -20% (29, 41%) |
| no_stop_tp100 | -52% (501, 19%) | -20% (626, 7%) | -13% (4, 25%) | -18% (29, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 19128. Outcomes:

- missed_window: 12684
- low_liquidity: 3519
- proven_liquidity_gone: 1241
- no_momentum: 675
- research_failed: 521
- simulated failed buy: 216
- proven_low_volume: 177
- proven_price_collapsed_or_parabolic: 38
- proven: 30
- proven_no_uptrend: 19
- research_passed: 4
- dip: 4

Warning: 146 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
