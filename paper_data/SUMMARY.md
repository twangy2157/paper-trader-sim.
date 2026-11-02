# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T05:35:56Z. Bankroll cash (research-selected trades): 898.5. Open positions: 24. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 103 | 16% | -46.3% | -58 to -34 | -4777 |
| all momentum | 104 | 15% | -46.8% | -59 to -34 | -4878 |
| control | 72 | 11% | -15.3% | -25 to -5 | -1109 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -49% (83, 18%) | -15% (72, 11%) |
| wide_sl50_tp100 | -51% (83, 19%) | -16% (72, 11%) |
| sl30_tp50 | -51% (83, 22%) | -19% (72, 11%) |
| sl50_tp50 | -51% (83, 24%) | -18% (72, 12%) |
| no_stop_tp100 | -51% (83, 19%) | -16% (72, 11%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4172. Outcomes:

- missed_window: 2731
- low_liquidity: 1163
- no_momentum: 128
- research_failed: 115
- simulated failed buy: 34
- research_passed: 1

Warning: 24 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
