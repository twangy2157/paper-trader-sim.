# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T23:13:56Z. Bankroll cash (research-selected trades): 899.0. Open positions: 15. Pools on watchlist: 127.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 33 | 18% | -24.9% | [-46.2, -2.8] | -826.77 | 10 |
| all momentum entries | 34 | 18% | -27.1% | [-49.7, -5.1] | -927.77 | 10 |
| control (no momentum rule) | 10 | 20% | 2.4% | [-26.8, 32.6] | 21.71 | 5 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 13 | 38% | -11.4% |
| mom | wide_sl50_tp100 | 13 | 38% | -12.9% |
| mom | sl30_tp50 | 13 | 46% | -22.0% |
| mom | sl50_tp50 | 13 | 46% | -22.0% |
| mom | no_stop_tp100 | 13 | 38% | -11.3% |
| control | base_sl30_tp100 | 10 | 20% | 2.4% |
| control | wide_sl50_tp100 | 10 | 20% | 2.4% |
| control | sl30_tp50 | 10 | 20% | -6.9% |
| control | sl50_tp50 | 10 | 20% | -6.9% |
| control | no_stop_tp100 | 10 | 20% | 2.4% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 1971. Outcomes:

- missed_window: 1121
- low_liquidity: 732
- no_momentum: 63
- research_failed: 39
- simulated failed buy: 15
- research_passed: 1

Warning: 7 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
