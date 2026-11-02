# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T00:30:10Z. Bankroll cash (research-selected trades): 899.0. Open positions: 18. Pools on watchlist: 127.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 40 | 15% | -31.1% | [-50.5, -11.7] | -1247.09 | 10 |
| all momentum entries | 41 | 15% | -32.8% | [-51.8, -12.2] | -1348.09 | 10 |
| control (no momentum rule) | 22 | 14% | 0.5% | [-15.4, 16.5] | 7.17 | 6 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 20 | 25% | -28.4% |
| mom | wide_sl50_tp100 | 20 | 25% | -29.4% |
| mom | sl30_tp50 | 20 | 30% | -35.3% |
| mom | sl50_tp50 | 20 | 30% | -35.3% |
| mom | no_stop_tp100 | 20 | 25% | -28.4% |
| control | base_sl30_tp100 | 22 | 14% | 0.5% |
| control | wide_sl50_tp100 | 22 | 14% | 0.5% |
| control | sl30_tp50 | 22 | 14% | -5.4% |
| control | sl50_tp50 | 22 | 14% | -5.4% |
| control | no_stop_tp100 | 22 | 14% | 0.5% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 2555. Outcomes:

- missed_window: 1571
- low_liquidity: 843
- no_momentum: 72
- research_failed: 52
- simulated failed buy: 16
- research_passed: 1

Warning: 9 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
