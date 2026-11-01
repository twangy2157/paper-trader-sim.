# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T23:35:10Z. Bankroll cash (research-selected trades): 899.0. Open positions: 17. Pools on watchlist: 124.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 34 | 18% | -27.1% | [-49.5, -4.2] | -926.78 | 10 |
| all momentum entries | 35 | 17% | -29.2% | [-50.3, -6.6] | -1027.78 | 10 |
| control (no momentum rule) | 14 | 14% | -0.9% | [-21.7, 20.4] | -14.77 | 5 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 14 | 36% | -17.7% |
| mom | wide_sl50_tp100 | 14 | 36% | -19.1% |
| mom | sl30_tp50 | 14 | 43% | -27.6% |
| mom | sl50_tp50 | 14 | 43% | -27.6% |
| mom | no_stop_tp100 | 14 | 36% | -17.7% |
| control | base_sl30_tp100 | 14 | 14% | -0.9% |
| control | wide_sl50_tp100 | 14 | 14% | -0.9% |
| control | sl30_tp50 | 14 | 14% | -7.5% |
| control | sl50_tp50 | 14 | 14% | -7.5% |
| control | no_stop_tp100 | 14 | 14% | -0.9% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 2161. Outcomes:

- missed_window: 1275
- low_liquidity: 761
- no_momentum: 66
- research_failed: 43
- simulated failed buy: 15
- research_passed: 1

Warning: 7 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
