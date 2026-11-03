# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T01:03:43Z. Bankroll cash (research-selected trades): 898.5. Open positions: 18. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 204 | 15% | -52.0% | -60 to -43 | -10634 |
| all momentum | 205 | 15% | -52.3% | -61 to -43 | -10736 |
| control | 223 | 9% | -16.5% | -22 to -11 | -3703 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 3 | 0% | -100.0% | - | -300 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (184, 16%) | -17% (223, 9%) | - | -100% (3, 0%) |
| wide_sl50_tp100 | -55% (184, 17%) | -17% (223, 9%) | - | -100% (3, 0%) |
| sl30_tp50 | -55% (184, 20%) | -18% (223, 9%) | - | -100% (3, 0%) |
| sl50_tp50 | -55% (184, 22%) | -18% (223, 10%) | - | -100% (3, 0%) |
| no_stop_tp100 | -54% (184, 17%) | -17% (223, 9%) | - | -100% (3, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 8024. Outcomes:

- missed_window: 5324
- low_liquidity: 1838
- no_momentum: 278
- proven_liquidity_gone: 234
- research_failed: 210
- simulated failed buy: 76
- proven_low_volume: 46
- proven_price_collapsed_or_parabolic: 7
- proven_no_uptrend: 6
- proven: 4
- research_passed: 1

Warning: 54 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
