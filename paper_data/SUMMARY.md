# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T21:18:39Z. Bankroll cash (research-selected trades): 898.5. Open positions: 29. Pools on watchlist: 75.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 186 | 15% | -51.8% | -60 to -43 | -9647 |
| all momentum | 187 | 15% | -52.0% | -61 to -43 | -9749 |
| control | 175 | 11% | -16.3% | -23 to -10 | -2865 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (166, 16%) | -16% (175, 11%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -55% (166, 17%) | -17% (175, 11%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (166, 19%) | -18% (175, 11%) | - | -100% (1, 0%) |
| sl50_tp50 | -55% (166, 22%) | -18% (175, 12%) | - | -100% (1, 0%) |
| no_stop_tp100 | -54% (166, 18%) | -17% (175, 11%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 7039. Outcomes:

- missed_window: 4636
- low_liquidity: 1711
- no_momentum: 240
- research_failed: 192
- proven_liquidity_gone: 164
- simulated failed buy: 67
- proven_low_volume: 19
- proven: 3
- proven_no_uptrend: 3
- proven_price_collapsed_or_parabolic: 3
- research_passed: 1

Warning: 44 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
