# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T17:00:47Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2557 | 12% | -65.8% | -68 to -64 | -168603 |
| all momentum | 2573 | 12% | -65.6% | -68 to -63 | -169147 |
| control | 3271 | 6% | -18.8% | -20 to -18 | -61704 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 112 | 34% | -33.2% | -43 to -23 | -3725 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2552, 12%) | -19% (3271, 6%) | -12% (34, 29%) | -33% (112, 34%) |
| wide_sl50_tp100 | -66% (2552, 13%) | -19% (3271, 6%) | -15% (34, 32%) | -34% (112, 34%) |
| sl30_tp50 | -67% (2552, 14%) | -19% (3271, 7%) | -18% (34, 32%) | -33% (112, 35%) |
| sl50_tp50 | -67% (2552, 16%) | -19% (3271, 7%) | -21% (34, 35%) | -34% (112, 35%) |
| no_stop_tp100 | -66% (2552, 14%) | -19% (3271, 6%) | -13% (34, 32%) | -35% (112, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 88797. Outcomes:

- missed_window: 58304
- low_liquidity: 14555
- proven_liquidity_gone: 7417
- no_momentum: 3332
- research_failed: 2562
- proven_low_volume: 1173
- simulated failed buy: 1100
- proven_price_collapsed_or_parabolic: 137
- proven: 112
- proven_no_uptrend: 55
- dip: 34
- research_passed: 16

Warning: 699 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
