# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-02T01:34:30Z. Bankroll cash (research-selected trades): 899.0. Open positions: 15. Pools on watchlist: 118.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 52 | 15% | -33.5% | [-51.1, -14.3] | -1748.57 | 11 |
| all momentum entries | 53 | 15% | -34.8% | [-52.2, -15.8] | -1849.57 | 11 |
| control (no momentum rule) | 28 | 11% | -8.9% | [-24.2, 7.6] | -252.23 | 8 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 32 | 22% | -33.4% |
| mom | wide_sl50_tp100 | 32 | 22% | -35.6% |
| mom | sl30_tp50 | 32 | 25% | -40.7% |
| mom | sl50_tp50 | 32 | 25% | -42.2% |
| mom | no_stop_tp100 | 32 | 22% | -34.6% |
| control | base_sl30_tp100 | 28 | 11% | -8.9% |
| control | wide_sl50_tp100 | 28 | 11% | -9.4% |
| control | sl30_tp50 | 28 | 11% | -13.5% |
| control | sl50_tp50 | 28 | 11% | -14.1% |
| control | no_stop_tp100 | 28 | 11% | -10.0% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 3164. Outcomes:

- missed_window: 2063
- low_liquidity: 942
- no_momentum: 81
- research_failed: 58
- simulated failed buy: 19
- research_passed: 1

Warning: 11 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
