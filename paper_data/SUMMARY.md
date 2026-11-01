# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T21:24:00Z. Bankroll cash (research-selected trades): 899.0. Open positions: 7. Pools on watchlist: 107.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 23 | 9% | -34.0% | [-58.8, -8.9] | -785.81 | 8 |
| all momentum entries | 24 | 8% | -36.8% | [-60.5, -12.9] | -886.81 | 8 |
| control (no momentum rule) | 1 | 0% | -8.4% | - | -8.95 | 1 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 3 | 33% | -36.0% |
| mom | wide_sl50_tp100 | 3 | 33% | -36.0% |
| mom | sl30_tp50 | 3 | 33% | -51.9% |
| mom | sl50_tp50 | 3 | 33% | -51.9% |
| mom | no_stop_tp100 | 3 | 33% | -36.0% |
| control | base_sl30_tp100 | 1 | 0% | -8.4% |
| control | wide_sl50_tp100 | 1 | 0% | -8.4% |
| control | sl30_tp50 | 1 | 0% | -8.4% |
| control | sl50_tp50 | 1 | 0% | -8.4% |
| control | no_stop_tp100 | 1 | 0% | -8.4% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 1083. Outcomes:

- low_liquidity: 547
- missed_window: 451
- no_momentum: 48
- research_failed: 27
- simulated failed buy: 9
- research_passed: 1

Warning: 3 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
