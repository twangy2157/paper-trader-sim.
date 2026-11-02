# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T16:31:09Z. Bankroll cash (research-selected trades): 898.5. Open positions: 22. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 151 | 15% | -52.0% | -61 to -42 | -7863 |
| all momentum | 152 | 14% | -52.3% | -62 to -42 | -7965 |
| control | 131 | 11% | -15.3% | -22 to -9 | -2011 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (131, 16%) | -15% (131, 11%) | - | - |
| wide_sl50_tp100 | -55% (131, 18%) | -16% (131, 11%) | - | - |
| sl30_tp50 | -56% (131, 20%) | -17% (131, 11%) | - | - |
| sl50_tp50 | -55% (131, 22%) | -17% (131, 12%) | - | - |
| no_stop_tp100 | -56% (131, 18%) | -16% (131, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5635. Outcomes:

- missed_window: 3703
- low_liquidity: 1474
- no_momentum: 184
- research_failed: 164
- proven_liquidity_gone: 54
- simulated failed buy: 49
- proven_low_volume: 6
- research_passed: 1

Warning: 31 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
