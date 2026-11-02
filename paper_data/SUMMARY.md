# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T00:07:42Z. Bankroll cash (research-selected trades): 899.0. Open positions: 16. Pools on watchlist: 45.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 37 | 16% | -30.4% | [-50.7, -9.3] | -1131.10 | 10 |
| all momentum entries | 38 | 16% | -32.3% | [-52.7, -11.7] | -1232.10 | 10 |
| control (no momentum rule) | 18 | 11% | -2.1% | [-18.7, 18.8] | -40.65 | 6 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 17 | 29% | -26.6% |
| mom | wide_sl50_tp100 | 17 | 29% | -27.8% |
| mom | sl30_tp50 | 17 | 35% | -34.8% |
| mom | sl50_tp50 | 17 | 35% | -34.8% |
| mom | no_stop_tp100 | 17 | 29% | -26.6% |
| control | base_sl30_tp100 | 18 | 11% | -2.1% |
| control | wide_sl50_tp100 | 18 | 11% | -2.1% |
| control | sl30_tp50 | 18 | 11% | -7.3% |
| control | sl50_tp50 | 18 | 11% | -7.3% |
| control | no_stop_tp100 | 18 | 11% | -2.1% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 2437. Outcomes:

- missed_window: 1489
- low_liquidity: 816
- no_momentum: 68
- research_failed: 47
- simulated failed buy: 16
- research_passed: 1

Warning: 9 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
