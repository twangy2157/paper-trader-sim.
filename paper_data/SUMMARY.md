# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T14:45:30Z. Bankroll cash (research-selected trades): 898.5. Open positions: 25. Pools on watchlist: 102.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 134 | 14% | -50.3% | -61 to -40 | -6746 |
| all momentum | 135 | 14% | -50.6% | -61 to -40 | -6847 |
| control | 116 | 11% | -15.4% | -23 to -8 | -1801 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (114, 16%) | -15% (116, 11%) | - | - |
| wide_sl50_tp100 | -54% (114, 18%) | -16% (116, 11%) | - | - |
| sl30_tp50 | -54% (114, 19%) | -18% (116, 12%) | - | - |
| sl50_tp50 | -54% (114, 22%) | -17% (116, 13%) | - | - |
| no_stop_tp100 | -55% (114, 18%) | -17% (116, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 5036. Outcomes:

- missed_window: 3283
- low_liquidity: 1389
- no_momentum: 172
- research_failed: 147
- simulated failed buy: 44
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
