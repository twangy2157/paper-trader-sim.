# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T07:14:40Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 13. Pools on watchlist: 34.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 432 | 15% | -54.5% | -60 to -48 | -23592 |
| all momentum | 434 | 15% | -54.6% | -61 to -49 | -23732 |
| control | 512 | 8% | -16.8% | -20 to -14 | -8660 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 20 | 30% | -29.0% | -50 to -9 | -580 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (413, 15%) | -17% (512, 8%) | -13% (4, 25%) | -29% (20, 30%) |
| wide_sl50_tp100 | -56% (413, 17%) | -17% (512, 8%) | -13% (4, 25%) | -29% (20, 30%) |
| sl30_tp50 | -57% (413, 19%) | -17% (512, 9%) | -22% (4, 25%) | -29% (20, 30%) |
| sl50_tp50 | -57% (413, 21%) | -17% (512, 9%) | -22% (4, 25%) | -29% (20, 30%) |
| no_stop_tp100 | -55% (413, 18%) | -18% (512, 8%) | -13% (4, 25%) | -29% (20, 30%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16195. Outcomes:

- missed_window: 10769
- low_liquidity: 3072
- proven_liquidity_gone: 964
- no_momentum: 563
- research_failed: 437
- simulated failed buy: 176
- proven_low_volume: 151
- proven_price_collapsed_or_parabolic: 25
- proven: 21
- proven_no_uptrend: 11
- dip: 4
- research_passed: 2

Warning: 122 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
