# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T19:56:00Z. Bankroll cash (research-selected trades): 898.5. Open positions: 20. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 177 | 15% | -52.0% | -61 to -43 | -9216 |
| all momentum | 178 | 15% | -52.3% | -61 to -43 | -9318 |
| control | 160 | 11% | -15.6% | -22 to -9 | -2516 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (157, 17%) | -16% (160, 11%) | - | - |
| wide_sl50_tp100 | -55% (157, 18%) | -16% (160, 11%) | - | - |
| sl30_tp50 | -56% (157, 20%) | -18% (160, 12%) | - | - |
| sl50_tp50 | -56% (157, 22%) | -18% (160, 12%) | - | - |
| no_stop_tp100 | -54% (157, 18%) | -17% (160, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6603. Outcomes:

- missed_window: 4346
- low_liquidity: 1640
- no_momentum: 215
- research_failed: 185
- proven_liquidity_gone: 137
- simulated failed buy: 61
- proven_low_volume: 14
- proven_no_uptrend: 2
- research_passed: 1
- proven: 1
- proven_price_collapsed_or_parabolic: 1

Warning: 38 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
