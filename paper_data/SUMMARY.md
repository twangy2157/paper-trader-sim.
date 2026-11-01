# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T22:51:20Z. Bankroll cash (research-selected trades): 899.0. Open positions: 17. Pools on watchlist: 105.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 30 | 17% | -26.4% | [-49.5, -2.2] | -796.64 | 10 |
| all momentum entries | 31 | 16% | -28.8% | [-51.4, -4.4] | -897.64 | 10 |
| control (no momentum rule) | 6 | 0% | -8.5% | [-10.2, -6.4] | -52.93 | 4 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 10 | 40% | -11.8% |
| mom | wide_sl50_tp100 | 10 | 40% | -13.7% |
| mom | sl30_tp50 | 10 | 50% | -21.6% |
| mom | sl50_tp50 | 10 | 50% | -21.6% |
| mom | no_stop_tp100 | 10 | 40% | -11.6% |
| control | base_sl30_tp100 | 6 | 0% | -8.5% |
| control | wide_sl50_tp100 | 6 | 0% | -8.5% |
| control | sl30_tp50 | 6 | 0% | -8.5% |
| control | sl50_tp50 | 6 | 0% | -8.5% |
| control | no_stop_tp100 | 6 | 0% | -8.5% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 1781. Outcomes:

- missed_window: 968
- low_liquidity: 701
- no_momentum: 61
- research_failed: 36
- simulated failed buy: 14
- research_passed: 1

Warning: 6 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
