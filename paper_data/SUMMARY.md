# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T06:00:44Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2067 | 12% | -64.8% | -67 to -62 | -134197 |
| all momentum | 2083 | 12% | -64.6% | -67 to -62 | -134741 |
| control | 2831 | 6% | -18.0% | -19 to -17 | -51130 |
| dip buy | 29 | 24% | -20.4% | -41 to 2 | -593 |
| proven pools | 103 | 35% | -32.5% | -42 to -23 | -3358 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2062, 12%) | -18% (2831, 6%) | -20% (29, 24%) | -33% (103, 35%) |
| wide_sl50_tp100 | -65% (2062, 13%) | -18% (2831, 6%) | -24% (29, 28%) | -34% (103, 35%) |
| sl30_tp50 | -66% (2062, 15%) | -18% (2831, 6%) | -25% (29, 28%) | -32% (103, 36%) |
| sl50_tp50 | -66% (2062, 16%) | -19% (2831, 7%) | -28% (29, 31%) | -34% (103, 36%) |
| no_stop_tp100 | -65% (2062, 14%) | -18% (2831, 6%) | -22% (29, 28%) | -35% (103, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 73069. Outcomes:

- missed_window: 48176
- low_liquidity: 11791
- proven_liquidity_gone: 5859
- no_momentum: 2880
- research_failed: 2076
- proven_low_volume: 1065
- simulated failed buy: 910
- proven_price_collapsed_or_parabolic: 121
- proven: 103
- proven_no_uptrend: 42
- dip: 30
- research_passed: 16

Warning: 597 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
