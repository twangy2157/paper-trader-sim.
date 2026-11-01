# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T22:39:49Z. Bankroll cash (research-selected trades): 899.0. Open positions: 14. Pools on watchlist: 117.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 29 | 14% | -30.5% | [-53.0, -7.3] | -890.53 | 10 |
| all momentum entries | 30 | 13% | -32.9% | [-54.6, -9.3] | -991.53 | 10 |
| control (no momentum rule) | 6 | 0% | -8.5% | [-10.2, -6.4] | -52.93 | 4 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 9 | 33% | -23.5% |
| mom | wide_sl50_tp100 | 9 | 33% | -25.7% |
| mom | sl30_tp50 | 9 | 44% | -29.0% |
| mom | sl50_tp50 | 9 | 44% | -29.0% |
| mom | no_stop_tp100 | 9 | 33% | -23.3% |
| control | base_sl30_tp100 | 6 | 0% | -8.5% |
| control | wide_sl50_tp100 | 6 | 0% | -8.5% |
| control | sl30_tp50 | 6 | 0% | -8.5% |
| control | sl50_tp50 | 6 | 0% | -8.5% |
| control | no_stop_tp100 | 6 | 0% | -8.5% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 1685. Outcomes:

- missed_window: 898
- low_liquidity: 679
- no_momentum: 59
- research_failed: 34
- simulated failed buy: 14
- research_passed: 1

Warning: 6 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
