# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T21:08:33Z. Bankroll cash (research-selected trades): 898.5. Open positions: 25. Pools on watchlist: 68.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 186 | 15% | -51.8% | -60 to -43 | -9647 |
| all momentum | 187 | 15% | -52.0% | -61 to -43 | -9749 |
| control | 173 | 11% | -16.3% | -22 to -11 | -2842 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 1 | 0% | -100.0% | - | -100 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (166, 16%) | -16% (173, 11%) | - | -100% (1, 0%) |
| wide_sl50_tp100 | -55% (166, 17%) | -17% (173, 11%) | - | -100% (1, 0%) |
| sl30_tp50 | -56% (166, 19%) | -18% (173, 12%) | - | -100% (1, 0%) |
| sl50_tp50 | -55% (166, 22%) | -18% (173, 12%) | - | -100% (1, 0%) |
| no_stop_tp100 | -54% (166, 18%) | -17% (173, 11%) | - | -100% (1, 0%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6977. Outcomes:

- missed_window: 4592
- low_liquidity: 1706
- no_momentum: 235
- research_failed: 191
- proven_liquidity_gone: 158
- simulated failed buy: 66
- proven_low_volume: 19
- proven: 3
- proven_no_uptrend: 3
- proven_price_collapsed_or_parabolic: 3
- research_passed: 1

Warning: 43 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
