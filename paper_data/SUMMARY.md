# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T01:02:57Z. Bankroll cash (research-selected trades): 899.0. Open positions: 18. Pools on watchlist: 122.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 47 | 13% | -36.0% | [-54.1, -18.0] | -1696.57 | 11 |
| all momentum entries | 48 | 12% | -37.3% | [-54.7, -19.5] | -1797.57 | 11 |
| control (no momentum rule) | 24 | 12% | 0.1% | [-14.9, 15.0] | -1.51 | 7 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 27 | 19% | -37.7% |
| mom | wide_sl50_tp100 | 27 | 19% | -39.5% |
| mom | sl30_tp50 | 27 | 22% | -42.8% |
| mom | sl50_tp50 | 27 | 22% | -43.9% |
| mom | no_stop_tp100 | 27 | 19% | -38.1% |
| control | base_sl30_tp100 | 24 | 12% | 0.1% |
| control | wide_sl50_tp100 | 24 | 12% | 0.1% |
| control | sl30_tp50 | 24 | 12% | -5.3% |
| control | sl50_tp50 | 24 | 12% | -5.3% |
| control | no_stop_tp100 | 24 | 12% | 0.1% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 2860. Outcomes:

- missed_window: 1816
- low_liquidity: 892
- no_momentum: 78
- research_failed: 55
- simulated failed buy: 18
- research_passed: 1

Warning: 10 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
