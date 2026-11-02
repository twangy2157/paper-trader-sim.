# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T00:41:35Z. Bankroll cash (research-selected trades): 899.0. Open positions: 17. Pools on watchlist: 128.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 45 | 13% | -34.6% | [-52.9, -14.9] | -1560.39 | 10 |
| all momentum entries | 46 | 13% | -36.0% | [-53.6, -16.6] | -1661.39 | 10 |
| control (no momentum rule) | 22 | 14% | 0.5% | [-15.4, 16.5] | 7.17 | 6 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 25 | 20% | -35.3% |
| mom | wide_sl50_tp100 | 25 | 20% | -36.0% |
| mom | sl30_tp50 | 25 | 24% | -40.8% |
| mom | sl50_tp50 | 25 | 24% | -40.8% |
| mom | no_stop_tp100 | 25 | 20% | -35.3% |
| control | base_sl30_tp100 | 22 | 14% | 0.5% |
| control | wide_sl50_tp100 | 22 | 14% | 0.5% |
| control | sl30_tp50 | 22 | 14% | -5.4% |
| control | sl50_tp50 | 22 | 14% | -5.4% |
| control | no_stop_tp100 | 22 | 14% | 0.5% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 2660. Outcomes:

- missed_window: 1659
- low_liquidity: 856
- no_momentum: 75
- research_failed: 53
- simulated failed buy: 16
- research_passed: 1

Warning: 9 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
