# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T23:59:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2403 | 12% | -65.4% | -68 to -63 | -157293 |
| all momentum | 2419 | 12% | -65.2% | -68 to -63 | -157837 |
| control | 3132 | 6% | -18.7% | -20 to -17 | -58779 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 109 | 34% | -34.3% | -44 to -24 | -3744 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2398, 12%) | -19% (3132, 6%) | -15% (32, 28%) | -34% (109, 34%) |
| wide_sl50_tp100 | -65% (2398, 13%) | -19% (3132, 6%) | -18% (32, 31%) | -36% (109, 34%) |
| sl30_tp50 | -66% (2398, 15%) | -19% (3132, 7%) | -20% (32, 31%) | -34% (109, 35%) |
| sl50_tp50 | -66% (2398, 16%) | -19% (3132, 7%) | -23% (32, 34%) | -36% (109, 35%) |
| no_stop_tp100 | -65% (2398, 14%) | -19% (3132, 6%) | -16% (32, 31%) | -36% (109, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 84403. Outcomes:

- missed_window: 55444
- low_liquidity: 13875
- proven_liquidity_gone: 6982
- no_momentum: 3187
- research_failed: 2411
- proven_low_volume: 1133
- simulated failed buy: 1028
- proven_price_collapsed_or_parabolic: 134
- proven: 109
- proven_no_uptrend: 51
- dip: 33
- research_passed: 16

Warning: 653 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
