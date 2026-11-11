# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T12:44:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1732 | 12% | -64.9% | -67 to -62 | -112535 |
| all momentum | 1748 | 12% | -64.6% | -67 to -62 | -113079 |
| control | 2496 | 5% | -17.8% | -19 to -16 | -44634 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 83 | 35% | -28.9% | -41 to -18 | -2403 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1727, 12%) | -18% (2496, 5%) | -16% (20, 25%) | -29% (83, 35%) |
| wide_sl50_tp100 | -65% (1727, 13%) | -18% (2496, 6%) | -20% (20, 30%) | -30% (83, 35%) |
| sl30_tp50 | -66% (1727, 15%) | -18% (2496, 6%) | -26% (20, 25%) | -30% (83, 35%) |
| sl50_tp50 | -66% (1727, 16%) | -18% (2496, 7%) | -30% (20, 30%) | -31% (83, 35%) |
| no_stop_tp100 | -65% (1727, 14%) | -18% (2496, 6%) | -17% (20, 30%) | -30% (83, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 62223. Outcomes:

- missed_window: 41083
- low_liquidity: 10017
- proven_liquidity_gone: 4795
- no_momentum: 2552
- research_failed: 1740
- proven_low_volume: 977
- simulated failed buy: 795
- proven_price_collapsed_or_parabolic: 106
- proven: 85
- proven_no_uptrend: 37
- dip: 20
- research_passed: 16

Warning: 533 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
