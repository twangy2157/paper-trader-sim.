# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T11:17:56Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2300 | 12% | -64.9% | -67 to -63 | -149396 |
| all momentum | 2316 | 12% | -64.7% | -67 to -62 | -149940 |
| control | 3045 | 6% | -18.4% | -20 to -17 | -56234 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2295, 12%) | -18% (3045, 6%) | -15% (32, 28%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2295, 13%) | -19% (3045, 6%) | -18% (32, 31%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2295, 15%) | -19% (3045, 7%) | -20% (32, 31%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2295, 16%) | -19% (3045, 7%) | -23% (32, 34%) | -34% (107, 36%) |
| no_stop_tp100 | -65% (2295, 14%) | -19% (3045, 6%) | -16% (32, 31%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 80408. Outcomes:

- missed_window: 52688
- low_liquidity: 13234
- proven_liquidity_gone: 6637
- no_momentum: 3101
- research_failed: 2312
- proven_low_volume: 1111
- simulated failed buy: 992
- proven_price_collapsed_or_parabolic: 130
- proven: 107
- proven_no_uptrend: 48
- dip: 32
- research_passed: 16

Warning: 641 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
