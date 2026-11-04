# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T01:05:55Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 6. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 389 | 14% | -54.5% | -61 to -48 | -21249 |
| all momentum | 391 | 14% | -54.6% | -61 to -48 | -21389 |
| control | 464 | 8% | -16.0% | -19 to -13 | -7472 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 18 | 33% | -31.9% | -56 to -9 | -575 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (370, 15%) | -16% (464, 8%) | -13% (4, 25%) | -32% (18, 33%) |
| wide_sl50_tp100 | -56% (370, 16%) | -16% (464, 8%) | -13% (4, 25%) | -32% (18, 33%) |
| sl30_tp50 | -57% (370, 19%) | -17% (464, 8%) | -22% (4, 25%) | -32% (18, 33%) |
| sl50_tp50 | -57% (370, 21%) | -17% (464, 8%) | -22% (4, 25%) | -32% (18, 33%) |
| no_stop_tp100 | -55% (370, 17%) | -17% (464, 8%) | -13% (4, 25%) | -32% (18, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 14433. Outcomes:

- missed_window: 9584
- low_liquidity: 2789
- proven_liquidity_gone: 802
- no_momentum: 509
- research_failed: 393
- simulated failed buy: 158
- proven_low_volume: 143
- proven_price_collapsed_or_parabolic: 20
- proven: 19
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 108 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
