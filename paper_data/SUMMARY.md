# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T01:13:00Z. Bankroll cash (research-selected trades): 899.0. Open positions: 20. Pools on watchlist: 141.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 48 | 12% | -35.9% | [-53.0, -18.0] | -1730.93 | 11 |
| all momentum entries | 49 | 12% | -37.3% | [-54.7, -18.9] | -1831.93 | 11 |
| control (no momentum rule) | 24 | 12% | 0.1% | [-14.9, 15.0] | -2.01 | 8 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 28 | 18% | -37.6% |
| mom | wide_sl50_tp100 | 28 | 18% | -40.0% |
| mom | sl30_tp50 | 28 | 21% | -42.5% |
| mom | sl50_tp50 | 28 | 21% | -44.3% |
| mom | no_stop_tp100 | 28 | 18% | -38.9% |
| control | base_sl30_tp100 | 24 | 12% | 0.1% |
| control | wide_sl50_tp100 | 24 | 12% | 0.1% |
| control | sl30_tp50 | 24 | 12% | -5.3% |
| control | sl50_tp50 | 24 | 12% | -5.3% |
| control | no_stop_tp100 | 24 | 12% | 0.1% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 2948. Outcomes:

- missed_window: 1881
- low_liquidity: 911
- no_momentum: 80
- research_failed: 56
- simulated failed buy: 19
- research_passed: 1

Warning: 11 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
