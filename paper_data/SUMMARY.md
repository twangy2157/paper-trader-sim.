# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-01T23:02:39Z. Bankroll cash (research-selected trades): 899.0. Open positions: 14. Pools on watchlist: 119.

| group | closed | win rate | avg return | 95% CI of avg | total P&L $ | failed buys |
|---|---|---|---|---|---|---|
| filter=1 (research-selected) | 1 | 0% | -101.0% | - | -101.00 | 0 |
| filter=0 (momentum only) | 32 | 19% | -22.6% | [-44.2, 0.3] | -728.12 | 10 |
| all momentum entries | 33 | 18% | -25.0% | [-46.2, -3.1] | -829.12 | 10 |
| control (no momentum rule) | 9 | 11% | -6.7% | [-37.5, 25.5] | -62.73 | 4 |

What-if exit rules on the SAME trades (stop-loss / take-profit):

| group | exit rule | trades | win rate | avg return |
|---|---|---|---|---|
| mom | base_sl30_tp100 | 12 | 42% | -4.1% |
| mom | wide_sl50_tp100 | 12 | 42% | -5.7% |
| mom | sl30_tp50 | 12 | 50% | -15.6% |
| mom | sl50_tp50 | 12 | 50% | -15.6% |
| mom | no_stop_tp100 | 12 | 42% | -3.9% |
| control | base_sl30_tp100 | 9 | 11% | -6.7% |
| control | wide_sl50_tp100 | 9 | 11% | -6.7% |
| control | sl30_tp50 | 9 | 11% | -12.1% |
| control | sl50_tp50 | 9 | 11% | -12.1% |
| control | no_stop_tp100 | 9 | 11% | -6.7% |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 1868. Outcomes:

- missed_window: 1038
- low_liquidity: 716
- no_momentum: 62
- research_failed: 37
- simulated failed buy: 14
- research_passed: 1

Warning: 6 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
