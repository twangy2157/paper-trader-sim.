# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T06:34:09Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 20. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 428 | 15% | -54.1% | -60 to -48 | -23193 |
| all momentum | 430 | 15% | -54.2% | -60 to -48 | -23333 |
| control | 509 | 8% | -16.7% | -20 to -13 | -8573 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (409, 16%) | -17% (509, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (409, 17%) | -17% (509, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (409, 19%) | -17% (509, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (409, 21%) | -17% (509, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (409, 18%) | -18% (509, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16134. Outcomes:

- missed_window: 10716
- low_liquidity: 3072
- proven_liquidity_gone: 958
- no_momentum: 562
- research_failed: 437
- simulated failed buy: 176
- proven_low_volume: 150
- proven_price_collapsed_or_parabolic: 25
- proven: 21
- proven_no_uptrend: 11
- dip: 4
- research_passed: 2

Warning: 122 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
