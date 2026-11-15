# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T02:23:42Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 78.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2414 | 12% | -65.4% | -68 to -63 | -158200 |
| all momentum | 2430 | 12% | -65.2% | -68 to -63 | -158744 |
| control | 3147 | 6% | -18.7% | -20 to -17 | -59159 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 109 | 34% | -34.3% | -44 to -24 | -3744 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2409, 12%) | -19% (3147, 6%) | -12% (33, 30%) | -34% (109, 34%) |
| wide_sl50_tp100 | -65% (2409, 13%) | -19% (3147, 6%) | -15% (33, 33%) | -36% (109, 34%) |
| sl30_tp50 | -67% (2409, 14%) | -19% (3147, 7%) | -18% (33, 33%) | -34% (109, 35%) |
| sl50_tp50 | -66% (2409, 16%) | -19% (3147, 7%) | -21% (33, 36%) | -36% (109, 35%) |
| no_stop_tp100 | -65% (2409, 14%) | -19% (3147, 6%) | -13% (33, 33%) | -36% (109, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 85028. Outcomes:

- missed_window: 55890
- low_liquidity: 13953
- proven_liquidity_gone: 7041
- no_momentum: 3202
- research_failed: 2425
- proven_low_volume: 1138
- simulated failed buy: 1034
- proven_price_collapsed_or_parabolic: 134
- proven: 110
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 656 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
