# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T00:51:39Z. Bankroll cash (research-selected trades): 899.0. Open positions: 17. Pools on watchlist: 129.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 46 | 13% | -34.6% | [-52.7, -17.0] | -1595.57 | 11 |
| all momentum entries | 47 | 13% | -36.0% | [-53.5, -17.9] | -1696.57 | 11 |
| control (no momentum rule) | 22 | 14% | 0.5% | [-15.4, 16.5] | 7.17 | 6 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 26 | 19% | -35.2% |
| mom | wide_sl50_tp100 | 26 | 19% | -37.2% |
| mom | sl30_tp50 | 26 | 23% | -40.6% |
| mom | sl50_tp50 | 26 | 23% | -41.7% |
| mom | no_stop_tp100 | 26 | 19% | -35.7% |
| control | base_sl30_tp100 | 22 | 14% | 0.5% |
| control | wide_sl50_tp100 | 22 | 14% | 0.5% |
| control | sl30_tp50 | 22 | 14% | -5.4% |
| control | sl50_tp50 | 22 | 14% | -5.4% |
| control | no_stop_tp100 | 22 | 14% | 0.5% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 2746. Outcomes:

- missed_window: 1723
- low_liquidity: 876
- no_momentum: 75
- research_failed: 54
- simulated failed buy: 17
- research_passed: 1

Warning: 9 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
