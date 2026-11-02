# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T19:12:56Z. Bankroll cash (research-selected trades): 898.5. Open positions: 17. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 174 | 15% | -52.3% | -61 to -44 | -9110 |
| all momentum | 175 | 15% | -52.6% | -61 to -44 | -9211 |
| control | 155 | 12% | -14.9% | -21 to -8 | -2319 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (154, 16%) | -15% (155, 12%) | - | - |
| wide_sl50_tp100 | -55% (154, 18%) | -16% (155, 12%) | - | - |
| sl30_tp50 | -56% (154, 19%) | -17% (155, 12%) | - | - |
| sl50_tp50 | -56% (154, 21%) | -17% (155, 13%) | - | - |
| no_stop_tp100 | -55% (154, 18%) | -16% (155, 12%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6411. Outcomes:

- missed_window: 4238
- low_liquidity: 1596
- no_momentum: 208
- research_failed: 181
- proven_liquidity_gone: 117
- simulated failed buy: 57
- proven_low_volume: 9
- proven_no_uptrend: 2
- research_passed: 1
- proven: 1
- proven_price_collapsed_or_parabolic: 1

Warning: 36 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
