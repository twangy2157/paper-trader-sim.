# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T21:46:43Z. Bankroll cash (research-selected trades): 899.0. Open positions: 11. Pools on watchlist: 88.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 24 | 8% | -36.7% | [-60.7, -9.4] | -886.33 | 9 |
| all momentum entries | 25 | 8% | -39.3% | [-62.4, -15.9] | -987.33 | 9 |
| control (no momentum rule) | 1 | 0% | -8.4% | - | -8.95 | 1 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 4 | 25% | -52.0% |
| mom | wide_sl50_tp100 | 4 | 25% | -52.0% |
| mom | sl30_tp50 | 4 | 25% | -63.9% |
| mom | sl50_tp50 | 4 | 25% | -63.9% |
| mom | no_stop_tp100 | 4 | 25% | -52.0% |
| control | base_sl30_tp100 | 1 | 0% | -8.4% |
| control | wide_sl50_tp100 | 1 | 0% | -8.4% |
| control | sl30_tp50 | 1 | 0% | -8.4% |
| control | sl50_tp50 | 1 | 0% | -8.4% |
| control | no_stop_tp100 | 1 | 0% | -8.4% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 1278. Outcomes:

- missed_window: 596
- low_liquidity: 591
- no_momentum: 50
- research_failed: 30
- simulated failed buy: 10
- research_passed: 1

Warning: 3 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
