# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T19:23:08Z. Bankroll cash (research-selected trades): 898.5. Open positions: 16. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 175 | 15% | -52.5% | -61 to -43 | -9211 |
| all momentum | 176 | 15% | -52.8% | -61 to -44 | -9312 |
| control | 157 | 11% | -14.7% | -21 to -8 | -2324 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (155, 16%) | -15% (157, 11%) | - | - |
| wide_sl50_tp100 | -56% (155, 17%) | -15% (157, 11%) | - | - |
| sl30_tp50 | -56% (155, 19%) | -17% (157, 12%) | - | - |
| sl50_tp50 | -56% (155, 21%) | -17% (157, 13%) | - | - |
| no_stop_tp100 | -55% (155, 18%) | -16% (157, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6463. Outcomes:

- missed_window: 4271
- low_liquidity: 1605
- no_momentum: 210
- research_failed: 181
- proven_liquidity_gone: 122
- simulated failed buy: 60
- proven_low_volume: 9
- proven_no_uptrend: 2
- research_passed: 1
- proven: 1
- proven_price_collapsed_or_parabolic: 1

Warning: 37 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
