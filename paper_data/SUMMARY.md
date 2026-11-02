# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T06:07:41Z. Bankroll cash (research-selected trades): 898.5. Open positions: 26. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 108 | 15% | -46.8% | -58 to -35 | -5061 |
| all momentum | 109 | 15% | -47.3% | -59 to -36 | -5162 |
| control | 79 | 10% | -17.8% | -28 to -9 | -1413 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -50% (88, 17%) | -18% (79, 10%) |
| wide_sl50_tp100 | -51% (88, 18%) | -19% (79, 10%) |
| sl30_tp50 | -52% (88, 20%) | -21% (79, 10%) |
| sl50_tp50 | -52% (88, 23%) | -20% (79, 11%) |
| no_stop_tp100 | -52% (88, 18%) | -19% (79, 10%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4289. Outcomes:

- missed_window: 2797
- low_liquidity: 1198
- no_momentum: 138
- research_failed: 119
- simulated failed buy: 36
- research_passed: 1

Warning: 26 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
