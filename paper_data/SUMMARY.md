# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T22:34:39Z. Bankroll cash (research-selected trades): 898.5. Open positions: 19. Pools on watchlist: 52.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 193 | 15% | -52.8% | -61 to -44 | -10208 |
| all momentum | 194 | 14% | -53.1% | -61 to -44 | -10309 |
| control | 198 | 10% | -15.8% | -21 to -10 | -3145 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (173, 16%) | -16% (198, 10%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -56% (173, 17%) | -16% (198, 10%) | - | -100% (1, 0%) |
| sl30_tp50 | -57% (173, 19%) | -17% (198, 10%) | - | -100% (1, 0%) |
| sl50_tp50 | -56% (173, 21%) | -17% (198, 11%) | - | -100% (1, 0%) |
| no_stop_tp100 | -55% (173, 17%) | -17% (198, 10%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7492. Outcomes:

- missed_window: 4974
- low_liquidity: 1759
- no_momentum: 252
- research_failed: 200
- proven_liquidity_gone: 194
- simulated failed buy: 70
- proven_low_volume: 30
- proven_no_uptrend: 5
- proven_price_collapsed_or_parabolic: 4
- proven: 3
- research_passed: 1

Warning: 48 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
