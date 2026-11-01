# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T21:58:00Z. Bankroll cash (research-selected trades): 899.0. Open positions: 11. Pools on watchlist: 98.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 26 | 12% | -31.6% | [-54.8, -8.0] | -826.81 | 9 |
| all momentum entries | 27 | 11% | -34.2% | [-58.3, -9.3] | -927.81 | 9 |
| control (no momentum rule) | 3 | 0% | -8.4% | - | -26.18 | 2 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 6 | 33% | -24.8% |
| mom | wide_sl50_tp100 | 6 | 33% | -28.0% |
| mom | sl30_tp50 | 6 | 50% | -28.0% |
| mom | sl50_tp50 | 6 | 50% | -28.0% |
| mom | no_stop_tp100 | 6 | 33% | -24.4% |
| control | base_sl30_tp100 | 3 | 0% | -8.4% |
| control | wide_sl50_tp100 | 3 | 0% | -8.4% |
| control | sl30_tp50 | 3 | 0% | -8.4% |
| control | sl50_tp50 | 3 | 0% | -8.4% |
| control | no_stop_tp100 | 3 | 0% | -8.4% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 1349. Outcomes:

- missed_window: 650
- low_liquidity: 603
- no_momentum: 53
- research_failed: 31
- simulated failed buy: 11
- research_passed: 1

Warning: 4 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
