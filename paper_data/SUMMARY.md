# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T12:44:21Z. Bankroll cash (research-selected trades): 549.8381952860861. Open positions: 13. Pools on watchlist: 51.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 852 | 14% | -59.5% | -63 to -55 | -50781 |
| all momentum | 861 | 14% | -59.3% | -63 to -55 | -51131 |
| control | 1013 | 7% | -20.0% | -22 to -17 | -20320 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 42 | 48% | -13.7% | -29 to 2 | -579 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (840, 14%) | -20% (1013, 7%) | -36% (8, 12%) | -14% (42, 48%) |
| wide_sl50_tp100 | -60% (840, 16%) | -20% (1013, 7%) | -40% (8, 12%) | -14% (42, 48%) |
| sl30_tp50 | -61% (840, 17%) | -20% (1013, 8%) | -40% (8, 12%) | -16% (42, 48%) |
| sl50_tp50 | -61% (840, 19%) | -21% (1013, 8%) | -44% (8, 12%) | -16% (42, 48%) |
| no_stop_tp100 | -59% (840, 17%) | -21% (1013, 7%) | -36% (8, 12%) | -14% (42, 48%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 29752. Outcomes:

- missed_window: 19356
- low_liquidity: 5398
- proven_liquidity_gone: 2293
- no_momentum: 1064
- research_failed: 854
- simulated failed buy: 356
- proven_low_volume: 292
- proven_price_collapsed_or_parabolic: 54
- proven: 44
- proven_no_uptrend: 22
- research_passed: 10
- dip: 9

Warning: 223 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
