# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T23:52:57Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 16. Pools on watchlist: 69.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 382 | 14% | -54.5% | -61 to -48 | -20867 |
| all momentum | 384 | 14% | -54.6% | -61 to -49 | -21007 |
| control | 455 | 7% | -16.3% | -20 to -13 | -7449 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 18 | 33% | -31.9% | -56 to -9 | -575 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (363, 15%) | -16% (455, 7%) | -13% (4, 25%) | -32% (18, 33%) |
| wide_sl50_tp100 | -56% (363, 17%) | -17% (455, 8%) | -13% (4, 25%) | -32% (18, 33%) |
| sl30_tp50 | -57% (363, 19%) | -17% (455, 8%) | -22% (4, 25%) | -32% (18, 33%) |
| sl50_tp50 | -56% (363, 21%) | -17% (455, 8%) | -22% (4, 25%) | -32% (18, 33%) |
| no_stop_tp100 | -56% (363, 17%) | -17% (455, 8%) | -13% (4, 25%) | -32% (18, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 14223. Outcomes:

- missed_window: 9443
- low_liquidity: 2754
- proven_liquidity_gone: 778
- no_momentum: 508
- research_failed: 388
- simulated failed buy: 155
- proven_low_volume: 142
- proven_price_collapsed_or_parabolic: 20
- proven: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 104 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
