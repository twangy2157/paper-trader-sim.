# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T16:37:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2348 | 12% | -65.2% | -68 to -63 | -153304 |
| all momentum | 2364 | 12% | -65.0% | -67 to -63 | -153847 |
| control | 3086 | 6% | -18.5% | -20 to -17 | -57329 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 108 | 34% | -33.6% | -44 to -24 | -3644 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2343, 12%) | -18% (3086, 6%) | -15% (32, 28%) | -34% (108, 34%) |
| wide_sl50_tp100 | -65% (2343, 13%) | -19% (3086, 6%) | -18% (32, 31%) | -35% (108, 34%) |
| sl30_tp50 | -66% (2343, 15%) | -19% (3086, 7%) | -20% (32, 31%) | -34% (108, 35%) |
| sl50_tp50 | -66% (2343, 16%) | -19% (3086, 7%) | -23% (32, 34%) | -35% (108, 35%) |
| no_stop_tp100 | -65% (2343, 14%) | -19% (3086, 6%) | -16% (32, 31%) | -36% (108, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 82020. Outcomes:

- missed_window: 53794
- low_liquidity: 13479
- proven_liquidity_gone: 6783
- no_momentum: 3138
- research_failed: 2359
- proven_low_volume: 1124
- simulated failed buy: 1004
- proven_price_collapsed_or_parabolic: 131
- proven: 109
- proven_no_uptrend: 51
- dip: 32
- research_passed: 16

Warning: 647 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
