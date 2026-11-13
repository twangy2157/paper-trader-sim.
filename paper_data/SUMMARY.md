# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T22:24:39Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2199 | 12% | -64.6% | -67 to -62 | -142242 |
| all momentum | 2215 | 12% | -64.4% | -67 to -62 | -142786 |
| control | 2951 | 6% | -18.3% | -20 to -17 | -54225 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 105 | 35% | -32.6% | -43 to -23 | -3437 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2194, 12%) | -18% (2951, 6%) | -18% (31, 26%) | -33% (105, 35%) |
| wide_sl50_tp100 | -65% (2194, 13%) | -19% (2951, 6%) | -21% (31, 29%) | -34% (105, 35%) |
| sl30_tp50 | -66% (2194, 15%) | -19% (2951, 6%) | -22% (31, 29%) | -33% (105, 36%) |
| sl50_tp50 | -66% (2194, 16%) | -19% (2951, 7%) | -25% (31, 32%) | -34% (105, 36%) |
| no_stop_tp100 | -65% (2194, 14%) | -19% (2951, 6%) | -19% (31, 29%) | -35% (105, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 77279. Outcomes:

- missed_window: 50811
- low_liquidity: 12587
- proven_liquidity_gone: 6300
- no_momentum: 3003
- research_failed: 2207
- proven_low_volume: 1090
- simulated failed buy: 956
- proven_price_collapsed_or_parabolic: 126
- proven: 107
- proven_no_uptrend: 45
- dip: 31
- research_passed: 16

Warning: 620 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
