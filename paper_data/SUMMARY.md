# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T22:03:48Z. Bankroll cash (research-selected trades): 898.5. Open positions: 20. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 190 | 15% | -52.3% | -61 to -43 | -9952 |
| all momentum | 191 | 15% | -52.5% | -61 to -44 | -10054 |
| control | 190 | 10% | -16.0% | -22 to -11 | -3066 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (170, 16%) | -16% (190, 10%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -55% (170, 17%) | -17% (190, 10%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (170, 19%) | -18% (190, 11%) | - | -100% (1, 0%) |
| sl50_tp50 | -55% (170, 22%) | -18% (190, 11%) | - | -100% (1, 0%) |
| no_stop_tp100 | -54% (170, 18%) | -17% (190, 10%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7319. Outcomes:

- missed_window: 4851
- low_liquidity: 1738
- no_momentum: 247
- research_failed: 195
- proven_liquidity_gone: 183
- simulated failed buy: 70
- proven_low_volume: 23
- proven_no_uptrend: 4
- proven_price_collapsed_or_parabolic: 4
- proven: 3
- research_passed: 1

Warning: 48 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
