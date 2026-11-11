# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T12:16:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1729 | 12% | -64.8% | -68 to -62 | -112235 |
| all momentum | 1745 | 12% | -64.5% | -67 to -62 | -112778 |
| control | 2493 | 5% | -17.8% | -19 to -16 | -44622 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 82 | 35% | -28.0% | -39 to -17 | -2302 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1724, 12%) | -18% (2493, 5%) | -16% (20, 25%) | -28% (82, 35%) |
| wide_sl50_tp100 | -65% (1724, 13%) | -18% (2493, 6%) | -20% (20, 30%) | -29% (82, 35%) |
| sl30_tp50 | -66% (1724, 15%) | -18% (2493, 6%) | -26% (20, 25%) | -29% (82, 35%) |
| sl50_tp50 | -65% (1724, 16%) | -18% (2493, 6%) | -30% (20, 30%) | -31% (82, 35%) |
| no_stop_tp100 | -65% (1724, 14%) | -18% (2493, 6%) | -17% (20, 30%) | -30% (82, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 62111. Outcomes:

- missed_window: 41017
- low_liquidity: 9998
- proven_liquidity_gone: 4780
- no_momentum: 2548
- research_failed: 1734
- proven_low_volume: 976
- simulated failed buy: 795
- proven_price_collapsed_or_parabolic: 106
- proven: 84
- proven_no_uptrend: 37
- dip: 20
- research_passed: 16

Warning: 533 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
