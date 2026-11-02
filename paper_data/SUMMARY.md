# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T18:18:08Z. Bankroll cash (research-selected trades): 898.5. Open positions: 14. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 171 | 15% | -52.1% | -61 to -43 | -8924 |
| all momentum | 172 | 15% | -52.4% | -62 to -43 | -9026 |
| control | 147 | 12% | -14.8% | -21 to -8 | -2186 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (151, 17%) | -15% (147, 12%) | - | - |
| wide_sl50_tp100 | -55% (151, 18%) | -16% (147, 12%) | - | - |
| sl30_tp50 | -56% (151, 20%) | -17% (147, 12%) | - | - |
| sl50_tp50 | -56% (151, 22%) | -17% (147, 13%) | - | - |
| no_stop_tp100 | -54% (151, 19%) | -16% (147, 12%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 6192. Outcomes:

- missed_window: 4089
- low_liquidity: 1558
- no_momentum: 200
- research_failed: 175
- proven_liquidity_gone: 100
- simulated failed buy: 57
- proven_low_volume: 9
- proven_no_uptrend: 2
- research_passed: 1
- proven: 1

Warning: 36 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
