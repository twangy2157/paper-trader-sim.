# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T05:46:09Z. Bankroll cash (research-selected trades): 898.5. Open positions: 22. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 105 | 15% | -45.7% | -57 to -33 | -4810 |
| all momentum | 106 | 15% | -46.3% | -58 to -35 | -4911 |
| control | 75 | 11% | -17.2% | -27 to -8 | -1296 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -49% (85, 18%) | -17% (75, 11%) |
| wide_sl50_tp100 | -50% (85, 19%) | -18% (75, 11%) |
| sl30_tp50 | -51% (85, 21%) | -20% (75, 11%) |
| sl50_tp50 | -50% (85, 24%) | -20% (75, 12%) |
| no_stop_tp100 | -50% (85, 19%) | -18% (75, 11%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4213. Outcomes:

- missed_window: 2756
- low_liquidity: 1175
- no_momentum: 131
- research_failed: 115
- simulated failed buy: 35
- research_passed: 1

Warning: 24 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
