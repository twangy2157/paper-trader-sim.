# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T21:01:38Z. Bankroll cash (research-selected trades): 899.0. Open positions: 6. Pools on watchlist: 94.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 22 | 9% | -31.0% | [-56.5, -5.2] | -684.79 | 6 |
| all momentum entries | 23 | 9% | -34.0% | [-58.6, -9.6] | -785.79 | 6 |
| control (no momentum rule) | 1 | 0% | -8.4% | - | -8.45 | 0 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 2 | 50% | -4.0% |
| mom | wide_sl50_tp100 | 2 | 50% | -4.0% |
| mom | sl30_tp50 | 2 | 50% | -27.9% |
| mom | sl50_tp50 | 2 | 50% | -27.9% |
| mom | no_stop_tp100 | 2 | 50% | -4.0% |
| control | base_sl30_tp100 | 1 | 0% | -8.4% |
| control | wide_sl50_tp100 | 1 | 0% | -8.4% |
| control | sl30_tp50 | 1 | 0% | -8.4% |
| control | sl50_tp50 | 1 | 0% | -8.4% |
| control | no_stop_tp100 | 1 | 0% | -8.4% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 923. Outcomes:

- low_liquidity: 507
- missed_window: 336
- no_momentum: 47
- research_failed: 26
- simulated failed buy: 6
- research_passed: 1

Warning: 1 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
