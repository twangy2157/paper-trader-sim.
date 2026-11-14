# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T14:50:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 107.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2333 | 12% | -65.1% | -67 to -63 | -152039 |
| all momentum | 2349 | 12% | -64.9% | -67 to -62 | -152583 |
| control | 3073 | 6% | -18.4% | -20 to -17 | -56950 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 108 | 34% | -33.6% | -44 to -24 | -3644 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2328, 12%) | -18% (3073, 6%) | -15% (32, 28%) | -34% (108, 34%) |
| wide_sl50_tp100 | -65% (2328, 13%) | -19% (3073, 6%) | -18% (32, 31%) | -35% (108, 34%) |
| sl30_tp50 | -66% (2328, 15%) | -19% (3073, 7%) | -20% (32, 31%) | -34% (108, 35%) |
| sl50_tp50 | -66% (2328, 16%) | -19% (3073, 7%) | -23% (32, 34%) | -35% (108, 35%) |
| no_stop_tp100 | -65% (2328, 14%) | -19% (3073, 6%) | -16% (32, 31%) | -36% (108, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 81415. Outcomes:

- missed_window: 53370
- low_liquidity: 13386
- proven_liquidity_gone: 6731
- no_momentum: 3126
- research_failed: 2341
- proven_low_volume: 1121
- simulated failed buy: 1002
- proven_price_collapsed_or_parabolic: 131
- proven: 109
- proven_no_uptrend: 50
- dip: 32
- research_passed: 16

Warning: 646 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
