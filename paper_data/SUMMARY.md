# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T17:49:58Z. Bankroll cash (research-selected trades): 913.731903378573. Open positions: 33. Pools on watchlist: 95.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 4 | 25% | -21.2% | - | -86 |
| momentum, not picked | 507 | 15% | -53.6% | -59 to -48 | -27217 |
| all momentum | 511 | 15% | -53.3% | -59 to -48 | -27303 |
| control | 609 | 7% | -18.9% | -22 to -16 | -11577 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 29 | 41% | -18.2% | -37 to -1 | -530 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (490, 16%) | -19% (609, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| wide_sl50_tp100 | -54% (490, 18%) | -19% (609, 7%) | -13% (4, 25%) | -18% (29, 41%) |
| sl30_tp50 | -56% (490, 19%) | -19% (609, 8%) | -22% (4, 25%) | -20% (29, 41%) |
| sl50_tp50 | -55% (490, 22%) | -19% (609, 9%) | -22% (4, 25%) | -20% (29, 41%) |
| no_stop_tp100 | -53% (490, 19%) | -20% (609, 7%) | -13% (4, 25%) | -18% (29, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18904. Outcomes:

- missed_window: 12503
- low_liquidity: 3507
- proven_liquidity_gone: 1219
- no_momentum: 672
- research_failed: 521
- simulated failed buy: 214
- proven_low_volume: 176
- proven_price_collapsed_or_parabolic: 36
- proven: 29
- proven_no_uptrend: 19
- research_passed: 4
- dip: 4

Warning: 145 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
