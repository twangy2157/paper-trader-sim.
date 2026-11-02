# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T00:19:00Z. Bankroll cash (research-selected trades): 899.0. Open positions: 17. Pools on watchlist: 105.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 39 | 15% | -31.7% | [-51.2, -12.0] | -1240.11 | 10 |
| all momentum entries | 40 | 15% | -33.4% | [-53.3, -12.7] | -1341.11 | 10 |
| control (no momentum rule) | 21 | 10% | -2.7% | [-17.1, 14.2] | -58.73 | 6 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 19 | 26% | -29.5% |
| mom | wide_sl50_tp100 | 19 | 26% | -30.6% |
| mom | sl30_tp50 | 19 | 32% | -36.8% |
| mom | sl50_tp50 | 19 | 32% | -36.8% |
| mom | no_stop_tp100 | 19 | 26% | -29.6% |
| control | base_sl30_tp100 | 21 | 10% | -2.7% |
| control | wide_sl50_tp100 | 21 | 10% | -2.7% |
| control | sl30_tp50 | 21 | 10% | -7.1% |
| control | sl50_tp50 | 21 | 10% | -7.1% |
| control | no_stop_tp100 | 21 | 10% | -2.7% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 2476. Outcomes:

- missed_window: 1513
- low_liquidity: 825
- no_momentum: 71
- research_failed: 50
- simulated failed buy: 16
- research_passed: 1

Warning: 9 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
