# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T02:57:41Z. Bankroll cash (research-selected trades): 899.0. Open positions: 41. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -101 |
| momentum, not picked | 62 | 15% | -37.7% | -53 to -22 | -2345 |
| all momentum | 63 | 14% | -38.7% | -54 to -24 | -2446 |
| control | 42 | 10% | -8.8% | -20 to 2 | -374 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control |
|---|---|---|
| base_sl30_tp100 | -40% (42, 19%) | -9% (42, 10%) |
| wide_sl50_tp100 | -39% (42, 21%) | -10% (42, 10%) |
| sl30_tp50 | -45% (42, 21%) | -12% (42, 10%) |
| sl50_tp50 | -45% (42, 24%) | -11% (42, 12%) |
| no_stop_tp100 | -39% (42, 21%) | -11% (42, 10%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3583. Outcomes:

- missed_window: 2356
- low_liquidity: 1015
- no_momentum: 104
- research_failed: 85
- simulated failed buy: 22
- research_passed: 1

Warning: 13 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
