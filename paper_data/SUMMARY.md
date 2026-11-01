# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T23:56:38Z. Bankroll cash (research-selected trades): 899.0. Open positions: 17. Pools on watchlist: 117.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 36 | 17% | -28.5% | [-49.6, -7.2] | -1031.07 | 10 |
| all momentum entries | 37 | 16% | -30.5% | [-50.5, -9.3] | -1132.07 | 10 |
| control (no momentum rule) | 17 | 12% | -2.0% | [-18.9, 15.9] | -36.05 | 5 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 16 | 31% | -22.0% |
| mom | wide_sl50_tp100 | 16 | 31% | -23.2% |
| mom | sl30_tp50 | 16 | 38% | -30.7% |
| mom | sl50_tp50 | 16 | 38% | -30.7% |
| mom | no_stop_tp100 | 16 | 31% | -22.0% |
| control | base_sl30_tp100 | 17 | 12% | -2.0% |
| control | wide_sl50_tp100 | 17 | 12% | -2.0% |
| control | sl30_tp50 | 17 | 12% | -7.4% |
| control | sl50_tp50 | 17 | 12% | -7.4% |
| control | no_stop_tp100 | 17 | 12% | -2.0% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 2334. Outcomes:

- missed_window: 1407
- low_liquidity: 797
- no_momentum: 67
- research_failed: 47
- simulated failed buy: 15
- research_passed: 1

Warning: 8 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
