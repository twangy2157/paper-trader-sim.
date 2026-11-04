# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T04:10:32Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 21. Pools on watchlist: 86.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 410 | 15% | -54.0% | -60 to -48 | -22157 |
| all momentum | 412 | 15% | -54.0% | -60 to -48 | -22297 |
| control | 483 | 8% | -16.4% | -20 to -13 | -7947 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 19 | 32% | -30.3% | -54 to -10 | -577 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (391, 16%) | -16% (483, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| wide_sl50_tp100 | -55% (391, 17%) | -17% (483, 8%) | -13% (4, 25%) | -30% (19, 32%) |
| sl30_tp50 | -57% (391, 19%) | -17% (483, 8%) | -22% (4, 25%) | -30% (19, 32%) |
| sl50_tp50 | -56% (391, 21%) | -17% (483, 9%) | -22% (4, 25%) | -30% (19, 32%) |
| no_stop_tp100 | -55% (391, 18%) | -17% (483, 8%) | -13% (4, 25%) | -30% (19, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 15305. Outcomes:

- missed_window: 10124
- low_liquidity: 2953
- proven_liquidity_gone: 898
- no_momentum: 536
- research_failed: 421
- simulated failed buy: 168
- proven_low_volume: 148
- proven_price_collapsed_or_parabolic: 21
- proven: 20
- proven_no_uptrend: 10
- dip: 4
- research_passed: 2

Warning: 116 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
