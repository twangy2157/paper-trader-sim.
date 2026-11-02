# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T14:34:10Z. Bankroll cash (research-selected trades): 898.5. Open positions: 25. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 131 | 14% | -51.3% | -61 to -41 | -6736 |
| all momentum | 132 | 14% | -51.7% | -61 to -42 | -6837 |
| control | 114 | 11% | -14.8% | -22 to -7 | -1693 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (111, 15%) | -15% (114, 11%) | - | - |
| wide_sl50_tp100 | -55% (111, 17%) | -16% (114, 11%) | - | - |
| sl30_tp50 | -55% (111, 19%) | -17% (114, 12%) | - | - |
| sl50_tp50 | -55% (111, 22%) | -17% (114, 13%) | - | - |
| no_stop_tp100 | -56% (111, 17%) | -16% (114, 11%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4992. Outcomes:

- missed_window: 3253
- low_liquidity: 1380
- no_momentum: 169
- research_failed: 145
- simulated failed buy: 44
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
