# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T20:06:29Z. Bankroll cash (research-selected trades): 898.5. Open positions: 20. Pools on watchlist: 39.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 179 | 15% | -52.2% | -61 to -43 | -9352 |
| all momentum | 180 | 15% | -52.4% | -61 to -43 | -9453 |
| control | 161 | 11% | -15.6% | -22 to -9 | -2523 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (159, 16%) | -16% (161, 11%) | - | - |
| wide_sl50_tp100 | -55% (159, 18%) | -16% (161, 11%) | - | - |
| sl30_tp50 | -56% (159, 19%) | -18% (161, 12%) | - | - |
| sl50_tp50 | -55% (159, 22%) | -18% (161, 12%) | - | - |
| no_stop_tp100 | -55% (159, 18%) | -17% (161, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6671. Outcomes:

- missed_window: 4392
- low_liquidity: 1652
- no_momentum: 217
- research_failed: 186
- proven_liquidity_gone: 142
- simulated failed buy: 61
- proven_low_volume: 16
- proven_no_uptrend: 2
- research_passed: 1
- proven: 1
- proven_price_collapsed_or_parabolic: 1

Warning: 38 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
