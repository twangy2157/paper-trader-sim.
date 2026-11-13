# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T22:47:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 12. Pools on watchlist: 62.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2204 | 12% | -64.5% | -67 to -62 | -142437 |
| all momentum | 2220 | 12% | -64.3% | -67 to -62 | -142981 |
| control | 2956 | 6% | -18.3% | -20 to -17 | -54263 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 105 | 35% | -32.6% | -43 to -23 | -3437 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2199, 12%) | -18% (2956, 6%) | -18% (31, 26%) | -33% (105, 35%) |
| wide_sl50_tp100 | -65% (2199, 14%) | -19% (2956, 6%) | -21% (31, 29%) | -34% (105, 35%) |
| sl30_tp50 | -66% (2199, 15%) | -19% (2956, 6%) | -22% (31, 29%) | -33% (105, 36%) |
| sl50_tp50 | -66% (2199, 16%) | -19% (2956, 7%) | -25% (31, 32%) | -34% (105, 36%) |
| no_stop_tp100 | -65% (2199, 14%) | -19% (2956, 6%) | -19% (31, 29%) | -35% (105, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 77358. Outcomes:

- missed_window: 50860
- low_liquidity: 12602
- proven_liquidity_gone: 6311
- no_momentum: 3005
- research_failed: 2209
- proven_low_volume: 1090
- simulated failed buy: 956
- proven_price_collapsed_or_parabolic: 126
- proven: 107
- proven_no_uptrend: 45
- dip: 31
- research_passed: 16

Warning: 620 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
