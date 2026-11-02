# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T22:45:41Z. Bankroll cash (research-selected trades): 898.5. Open positions: 16. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 195 | 14% | -52.8% | -61 to -44 | -10311 |
| all momentum | 196 | 14% | -53.0% | -62 to -45 | -10412 |
| control | 200 | 10% | -15.7% | -21 to -11 | -3158 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (175, 15%) | -16% (200, 10%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -56% (175, 17%) | -16% (200, 10%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (175, 19%) | -17% (200, 10%) | - | -100% (1, 0%) |
| sl50_tp50 | -56% (175, 21%) | -17% (200, 10%) | - | -100% (1, 0%) |
| no_stop_tp100 | -55% (175, 17%) | -16% (200, 10%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7539. Outcomes:

- missed_window: 5015
- low_liquidity: 1761
- no_momentum: 253
- research_failed: 200
- proven_liquidity_gone: 196
- simulated failed buy: 70
- proven_low_volume: 31
- proven_no_uptrend: 5
- proven_price_collapsed_or_parabolic: 4
- proven: 3
- research_passed: 1

Warning: 48 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
