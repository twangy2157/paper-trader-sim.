# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T19:33:29Z. Bankroll cash (research-selected trades): 898.5. Open positions: 15. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 176 | 15% | -51.7% | -61 to -42 | -9116 |
| all momentum | 177 | 15% | -52.0% | -61 to -42 | -9218 |
| control | 160 | 11% | -15.6% | -22 to -9 | -2515 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (156, 17%) | -16% (160, 11%) | - | - |
| wide_sl50_tp100 | -55% (156, 18%) | -16% (160, 11%) | - | - |
| sl30_tp50 | -56% (156, 20%) | -18% (160, 12%) | - | - |
| sl50_tp50 | -55% (156, 22%) | -18% (160, 12%) | - | - |
| no_stop_tp100 | -54% (156, 19%) | -17% (160, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6495. Outcomes:

- missed_window: 4285
- low_liquidity: 1613
- no_momentum: 212
- research_failed: 182
- proven_liquidity_gone: 127
- simulated failed buy: 60
- proven_low_volume: 11
- proven_no_uptrend: 2
- research_passed: 1
- proven: 1
- proven_price_collapsed_or_parabolic: 1

Warning: 37 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
