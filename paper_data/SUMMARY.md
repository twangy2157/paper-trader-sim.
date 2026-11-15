# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T16:39:26Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 32. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2555 | 12% | -65.9% | -68 to -64 | -168505 |
| all momentum | 2571 | 12% | -65.7% | -68 to -63 | -169048 |
| control | 3260 | 6% | -18.8% | -20 to -17 | -61454 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 112 | 34% | -33.2% | -43 to -23 | -3725 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2550, 12%) | -19% (3260, 6%) | -12% (34, 29%) | -33% (112, 34%) |
| wide_sl50_tp100 | -66% (2550, 13%) | -19% (3260, 6%) | -15% (34, 32%) | -34% (112, 34%) |
| sl30_tp50 | -67% (2550, 14%) | -19% (3260, 7%) | -18% (34, 32%) | -33% (112, 35%) |
| sl50_tp50 | -67% (2550, 16%) | -19% (3260, 7%) | -21% (34, 35%) | -34% (112, 35%) |
| no_stop_tp100 | -66% (2550, 14%) | -19% (3260, 6%) | -13% (34, 32%) | -35% (112, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 88705. Outcomes:

- missed_window: 58241
- low_liquidity: 14538
- proven_liquidity_gone: 7413
- no_momentum: 3329
- research_failed: 2562
- proven_low_volume: 1170
- simulated failed buy: 1098
- proven_price_collapsed_or_parabolic: 137
- proven: 112
- proven_no_uptrend: 55
- dip: 34
- research_passed: 16

Warning: 698 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
