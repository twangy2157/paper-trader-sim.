# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T00:12:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2211 | 12% | -64.5% | -67 to -62 | -142740 |
| all momentum | 2227 | 12% | -64.2% | -67 to -62 | -143283 |
| control | 2964 | 6% | -18.3% | -20 to -17 | -54437 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 106 | 35% | -32.4% | -42 to -22 | -3444 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2206, 12%) | -18% (2964, 6%) | -18% (31, 26%) | -32% (106, 35%) |
| wide_sl50_tp100 | -65% (2206, 14%) | -19% (2964, 6%) | -21% (31, 29%) | -34% (106, 35%) |
| sl30_tp50 | -66% (2206, 15%) | -19% (2964, 6%) | -22% (31, 29%) | -32% (106, 36%) |
| sl50_tp50 | -66% (2206, 16%) | -19% (2964, 7%) | -25% (31, 32%) | -34% (106, 36%) |
| no_stop_tp100 | -64% (2206, 14%) | -19% (2964, 6%) | -19% (31, 29%) | -35% (106, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 77691. Outcomes:

- missed_window: 51032
- low_liquidity: 12698
- proven_liquidity_gone: 6344
- no_momentum: 3015
- research_failed: 2220
- proven_low_volume: 1092
- simulated failed buy: 963
- proven_price_collapsed_or_parabolic: 126
- proven: 107
- proven_no_uptrend: 46
- dip: 32
- research_passed: 16

Warning: 623 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
