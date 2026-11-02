# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T13:07:39Z. Bankroll cash (research-selected trades): 898.5. Open positions: 15. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 125 | 14% | -49.6% | -60 to -39 | -6210 |
| all momentum | 126 | 14% | -50.0% | -60 to -39 | -6312 |
| control | 98 | 12% | -16.2% | -25 to -7 | -1601 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -53% (105, 16%) | -16% (98, 12%) | - | - |
| wide_sl50_tp100 | -54% (105, 17%) | -17% (98, 12%) | - | - |
| sl30_tp50 | -53% (105, 20%) | -19% (98, 12%) | - | - |
| sl50_tp50 | -53% (105, 22%) | -19% (98, 13%) | - | - |
| no_stop_tp100 | -55% (105, 17%) | -17% (98, 12%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4608. Outcomes:

- missed_window: 3015
- low_liquidity: 1268
- no_momentum: 153
- research_failed: 129
- simulated failed buy: 42
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
