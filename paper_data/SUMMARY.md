# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T14:23:56Z. Bankroll cash (research-selected trades): 898.5. Open positions: 28. Pools on watchlist: 78.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 129 | 14% | -51.1% | -61 to -40 | -6602 |
| all momentum | 130 | 14% | -51.5% | -61 to -41 | -6704 |
| control | 112 | 12% | -14.9% | -22 to -7 | -1674 |
| dip buy | 0 | - | - | - | 0 |
| proven pools | 0 | - | - | - | 0 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (109, 16%) | -15% (112, 12%) | - | - |
| wide_sl50_tp100 | -56% (109, 17%) | -16% (112, 12%) | - | - |
| sl30_tp50 | -55% (109, 19%) | -17% (112, 12%) | - | - |
| sl50_tp50 | -55% (109, 21%) | -17% (112, 13%) | - | - |
| no_stop_tp100 | -56% (109, 17%) | -16% (112, 12%) | - | - |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4933. Outcomes:

- missed_window: 3210
- low_liquidity: 1365
- no_momentum: 169
- research_failed: 144
- simulated failed buy: 44
- research_passed: 1

Warning: 28 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
