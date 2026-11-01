# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T22:29:37Z. Bankroll cash (research-selected trades): 899.0. Open positions: 17. Pools on watchlist: 123.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 27 | 15% | -28.7% | [-52.4, -3.3] | -780.41 | 10 |
| all momentum entries | 28 | 14% | -31.3% | [-53.9, -6.7] | -881.41 | 10 |
| control (no momentum rule) | 4 | 0% | -8.8% | - | -37.31 | 4 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 7 | 43% | -14.5% |
| mom | wide_sl50_tp100 | 7 | 43% | -17.3% |
| mom | sl30_tp50 | 7 | 57% | -21.6% |
| mom | sl50_tp50 | 7 | 57% | -21.6% |
| mom | no_stop_tp100 | 7 | 43% | -14.2% |
| control | base_sl30_tp100 | 4 | 0% | -8.8% |
| control | wide_sl50_tp100 | 4 | 0% | -8.8% |
| control | sl30_tp50 | 4 | 0% | -8.8% |
| control | sl50_tp50 | 4 | 0% | -8.8% |
| control | no_stop_tp100 | 4 | 0% | -8.8% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 1594. Outcomes:

- missed_window: 826
- low_liquidity: 661
- no_momentum: 58
- research_failed: 34
- simulated failed buy: 14
- research_passed: 1

Warning: 6 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
