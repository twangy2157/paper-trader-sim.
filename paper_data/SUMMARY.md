# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T21:52:12Z. Bankroll cash (research-selected trades): 898.5. Open positions: 20. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 189 | 15% | -52.0% | -61 to -43 | -9852 |
| all momentum | 190 | 15% | -52.3% | -61 to -44 | -9953 |
| control | 188 | 10% | -16.1% | -22 to -10 | -3052 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (169, 16%) | -16% (188, 10%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -55% (169, 17%) | -17% (188, 10%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (169, 20%) | -18% (188, 11%) | - | -100% (1, 0%) |
| sl50_tp50 | -55% (169, 22%) | -18% (188, 11%) | - | -100% (1, 0%) |
| no_stop_tp100 | -54% (169, 18%) | -17% (188, 10%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7260. Outcomes:

- missed_window: 4815
- low_liquidity: 1727
- no_momentum: 244
- research_failed: 195
- proven_liquidity_gone: 176
- simulated failed buy: 69
- proven_low_volume: 22
- proven_no_uptrend: 4
- proven_price_collapsed_or_parabolic: 4
- proven: 3
- research_passed: 1

Warning: 47 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
