# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T15:08:11Z. Bankroll cash (research-selected trades): 898.5. Open positions: 16. Pools on watchlist: 83.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 139 | 14% | -50.8% | -60 to -41 | -7069 |
| all momentum | 140 | 14% | -51.1% | -61 to -41 | -7171 |
| control | 121 | 11% | -15.3% | -22 to -8 | -1857 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (119, 16%) | -15% (121, 11%) | - | - |
| wide_sl50_tp100 | -54% (119, 18%) | -16% (121, 11%) | - | - |
| sl30_tp50 | -54% (119, 20%) | -17% (121, 12%) | - | - |
| sl50_tp50 | -54% (119, 23%) | -17% (121, 12%) | - | - |
| no_stop_tp100 | -55% (119, 18%) | -17% (121, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5203. Outcomes:

- missed_window: 3416
- low_liquidity: 1412
- no_momentum: 173
- research_failed: 147
- simulated failed buy: 45
- proven_liquidity_gone: 8
- research_passed: 1
- proven_low_volume: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
