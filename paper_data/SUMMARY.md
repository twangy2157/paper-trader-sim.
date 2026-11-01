# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T23:45:29Z. Bankroll cash (research-selected trades): 899.0. Open positions: 16. Pools on watchlist: 106.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 36 | 17% | -28.5% | [-49.6, -7.2] | -1031.07 | 10 |
| all momentum entries | 37 | 16% | -30.5% | [-50.5, -9.3] | -1132.07 | 10 |
| control (no momentum rule) | 15 | 13% | -1.3% | [-20.6, 18.9] | -22.33 | 5 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 16 | 31% | -22.0% |
| mom | wide_sl50_tp100 | 16 | 31% | -23.2% |
| mom | sl30_tp50 | 16 | 38% | -30.7% |
| mom | sl50_tp50 | 16 | 38% | -30.7% |
| mom | no_stop_tp100 | 16 | 31% | -22.0% |
| control | base_sl30_tp100 | 15 | 13% | -1.3% |
| control | wide_sl50_tp100 | 15 | 13% | -1.3% |
| control | sl30_tp50 | 15 | 13% | -7.5% |
| control | sl50_tp50 | 15 | 13% | -7.5% |
| control | no_stop_tp100 | 15 | 13% | -1.3% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 2252. Outcomes:

- missed_window: 1346
- low_liquidity: 779
- no_momentum: 66
- research_failed: 45
- simulated failed buy: 15
- research_passed: 1

Warning: 7 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
