# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T01:23:12Z. Bankroll cash (research-selected trades): 899.0. Open positions: 16. Pools on watchlist: 132.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 51 | 14% | -35.9% | [-53.0, -18.4] | -1836.79 | 11 |
| all momentum entries | 52 | 13% | -37.2% | [-54.6, -19.4] | -1937.79 | 11 |
| control (no momentum rule) | 27 | 11% | -8.8% | [-25.5, 7.6] | -242.29 | 8 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 31 | 19% | -37.3% |
| mom | wide_sl50_tp100 | 31 | 19% | -39.6% |
| mom | sl30_tp50 | 31 | 23% | -43.4% |
| mom | sl50_tp50 | 31 | 23% | -45.0% |
| mom | no_stop_tp100 | 31 | 19% | -38.6% |
| control | base_sl30_tp100 | 27 | 11% | -8.8% |
| control | wide_sl50_tp100 | 27 | 11% | -9.4% |
| control | sl30_tp50 | 27 | 11% | -13.6% |
| control | sl50_tp50 | 27 | 11% | -14.2% |
| control | no_stop_tp100 | 27 | 11% | -10.0% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3059. Outcomes:

- missed_window: 1979
- low_liquidity: 922
- no_momentum: 81
- research_failed: 57
- simulated failed buy: 19
- research_passed: 1

Warning: 11 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
