# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T06:22:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2070 | 12% | -64.8% | -67 to -62 | -134263 |
| all momentum | 2086 | 12% | -64.5% | -67 to -62 | -134807 |
| control | 2833 | 6% | -18.0% | -19 to -17 | -51174 |
| dip buy | 29 | 24% | -20.4% | -41 to 2 | -593 |
| proven pools | 103 | 35% | -32.5% | -42 to -23 | -3358 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2065, 12%) | -18% (2833, 6%) | -20% (29, 24%) | -33% (103, 35%) |
| wide_sl50_tp100 | -65% (2065, 13%) | -18% (2833, 6%) | -24% (29, 28%) | -34% (103, 35%) |
| sl30_tp50 | -66% (2065, 15%) | -18% (2833, 6%) | -25% (29, 28%) | -32% (103, 36%) |
| sl50_tp50 | -66% (2065, 16%) | -19% (2833, 7%) | -28% (29, 31%) | -34% (103, 36%) |
| no_stop_tp100 | -65% (2065, 14%) | -18% (2833, 6%) | -22% (29, 28%) | -35% (103, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 73167. Outcomes:

- missed_window: 48236
- low_liquidity: 11809
- proven_liquidity_gone: 5871
- no_momentum: 2883
- research_failed: 2078
- proven_low_volume: 1067
- simulated failed buy: 911
- proven_price_collapsed_or_parabolic: 121
- proven: 103
- proven_no_uptrend: 42
- dip: 30
- research_passed: 16

Warning: 598 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
