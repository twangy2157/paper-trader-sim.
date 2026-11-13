# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T22:36:12Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 33.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2201 | 12% | -64.6% | -67 to -62 | -142384 |
| all momentum | 2217 | 12% | -64.4% | -67 to -62 | -142928 |
| control | 2953 | 6% | -18.3% | -20 to -17 | -54238 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 105 | 35% | -32.6% | -43 to -23 | -3437 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2196, 12%) | -18% (2953, 6%) | -18% (31, 26%) | -33% (105, 35%) |
| wide_sl50_tp100 | -65% (2196, 14%) | -19% (2953, 6%) | -21% (31, 29%) | -34% (105, 35%) |
| sl30_tp50 | -66% (2196, 15%) | -19% (2953, 6%) | -22% (31, 29%) | -33% (105, 36%) |
| sl50_tp50 | -66% (2196, 16%) | -19% (2953, 7%) | -25% (31, 32%) | -34% (105, 36%) |
| no_stop_tp100 | -65% (2196, 14%) | -19% (2953, 6%) | -19% (31, 29%) | -35% (105, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 77335. Outcomes:

- missed_window: 50849
- low_liquidity: 12596
- proven_liquidity_gone: 6307
- no_momentum: 3004
- research_failed: 2208
- proven_low_volume: 1090
- simulated failed buy: 956
- proven_price_collapsed_or_parabolic: 126
- proven: 107
- proven_no_uptrend: 45
- dip: 31
- research_passed: 16

Warning: 620 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
