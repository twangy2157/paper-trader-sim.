# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T19:09:20Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 31.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2370 | 12% | -65.3% | -68 to -63 | -154939 |
| all momentum | 2386 | 12% | -65.1% | -67 to -63 | -155483 |
| control | 3102 | 6% | -18.5% | -20 to -17 | -57666 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 109 | 34% | -34.3% | -44 to -24 | -3744 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2365, 12%) | -19% (3102, 6%) | -15% (32, 28%) | -34% (109, 34%) |
| wide_sl50_tp100 | -65% (2365, 13%) | -19% (3102, 6%) | -18% (32, 31%) | -36% (109, 34%) |
| sl30_tp50 | -66% (2365, 15%) | -19% (3102, 7%) | -20% (32, 31%) | -34% (109, 35%) |
| sl50_tp50 | -66% (2365, 16%) | -19% (3102, 7%) | -23% (32, 34%) | -36% (109, 35%) |
| no_stop_tp100 | -65% (2365, 14%) | -19% (3102, 6%) | -16% (32, 31%) | -36% (109, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 82740. Outcomes:

- missed_window: 54292
- low_liquidity: 13588
- proven_liquidity_gone: 6846
- no_momentum: 3155
- research_failed: 2375
- proven_low_volume: 1128
- simulated failed buy: 1016
- proven_price_collapsed_or_parabolic: 132
- proven: 109
- proven_no_uptrend: 51
- dip: 32
- research_passed: 16

Warning: 650 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
