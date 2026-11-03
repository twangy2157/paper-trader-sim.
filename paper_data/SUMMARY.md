# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T23:32:36Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 20. Pools on watchlist: 69.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 378 | 15% | -54.6% | -61 to -48 | -20660 |
| all momentum | 380 | 14% | -54.6% | -61 to -48 | -20799 |
| control | 452 | 8% | -16.3% | -20 to -13 | -7424 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 18 | 33% | -31.9% | -56 to -9 | -575 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (359, 15%) | -16% (452, 8%) | -13% (4, 25%) | -32% (18, 33%) |
| wide_sl50_tp100 | -56% (359, 17%) | -17% (452, 8%) | -13% (4, 25%) | -32% (18, 33%) |
| sl30_tp50 | -57% (359, 19%) | -17% (452, 8%) | -22% (4, 25%) | -32% (18, 33%) |
| sl50_tp50 | -57% (359, 21%) | -17% (452, 8%) | -22% (4, 25%) | -32% (18, 33%) |
| no_stop_tp100 | -56% (359, 17%) | -17% (452, 8%) | -13% (4, 25%) | -32% (18, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 14116. Outcomes:

- missed_window: 9369
- low_liquidity: 2738
- proven_liquidity_gone: 770
- no_momentum: 507
- research_failed: 386
- simulated failed buy: 152
- proven_low_volume: 139
- proven_price_collapsed_or_parabolic: 20
- proven: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 102 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
