# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T19:44:41Z. Bankroll cash (research-selected trades): 898.5. Open positions: 15. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 177 | 15% | -52.0% | -61 to -43 | -9216 |
| all momentum | 178 | 15% | -52.3% | -61 to -43 | -9318 |
| control | 160 | 11% | -15.6% | -22 to -9 | -2515 |
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

Pools seen: 6552. Outcomes:

- missed_window: 4319
- low_liquidity: 1628
- no_momentum: 212
- research_failed: 183
- proven_liquidity_gone: 132
- simulated failed buy: 60
- proven_low_volume: 13
- proven_no_uptrend: 2
- research_passed: 1
- proven: 1
- proven_price_collapsed_or_parabolic: 1

Warning: 37 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
