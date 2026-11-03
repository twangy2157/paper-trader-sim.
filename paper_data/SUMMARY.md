# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T03:41:38Z. Bankroll cash (research-selected trades): 898.0. Open positions: 22. Pools on watchlist: 68.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 224 | 15% | -51.9% | -60 to -43 | -11653 |
| all momentum | 225 | 15% | -52.1% | -60 to -43 | -11755 |
| control | 251 | 8% | -16.3% | -21 to -12 | -4102 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 4 | 0% | -100.3% | - | -401 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (204, 16%) | -16% (251, 8%) | - | -100% (4, 0%) |
| wide_sl50_tp100 | -54% (204, 17%) | -17% (251, 8%) | - | -100% (4, 0%) |
| sl30_tp50 | -56% (204, 19%) | -18% (251, 9%) | - | -100% (4, 0%) |
| sl50_tp50 | -55% (204, 21%) | -18% (251, 9%) | - | -100% (4, 0%) |
| no_stop_tp100 | -54% (204, 17%) | -17% (251, 8%) | - | -100% (4, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8790. Outcomes:

- missed_window: 5831
- low_liquidity: 1950
- no_momentum: 307
- proven_liquidity_gone: 297
- research_failed: 233
- simulated failed buy: 91
- proven_low_volume: 60
- proven_price_collapsed_or_parabolic: 9
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1
- dip: 1

Warning: 60 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
