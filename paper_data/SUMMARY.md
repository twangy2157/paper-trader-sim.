# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T05:14:40Z. Bankroll cash (research-selected trades): 899.0. Open positions: 27. Pools on watchlist: 48.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 98 | 15% | -46.8% | -59 to -34 | -4594 |
| all momentum | 99 | 15% | -47.4% | -59 to -35 | -4695 |
| control | 67 | 12% | -12.7% | -23 to -2 | -861 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -50% (78, 18%) | -13% (67, 12%) |
| wide_sl50_tp100 | -52% (78, 19%) | -14% (67, 12%) |
| sl30_tp50 | -52% (78, 22%) | -16% (67, 12%) |
| sl50_tp50 | -52% (78, 24%) | -16% (67, 13%) |
| no_stop_tp100 | -52% (78, 19%) | -14% (67, 12%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 4082. Outcomes:

- missed_window: 2666
- low_liquidity: 1147
- no_momentum: 126
- research_failed: 110
- simulated failed buy: 32
- research_passed: 1

Warning: 23 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
