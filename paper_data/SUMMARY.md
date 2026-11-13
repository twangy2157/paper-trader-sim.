# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T23:18:53Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 37.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2206 | 12% | -64.6% | -67 to -62 | -142639 |
| all momentum | 2222 | 12% | -64.3% | -67 to -62 | -143182 |
| control | 2959 | 6% | -18.3% | -20 to -17 | -54370 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 105 | 35% | -32.6% | -43 to -23 | -3437 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2201, 12%) | -18% (2959, 6%) | -18% (31, 26%) | -33% (105, 35%) |
| wide_sl50_tp100 | -65% (2201, 14%) | -19% (2959, 6%) | -21% (31, 29%) | -34% (105, 35%) |
| sl30_tp50 | -66% (2201, 15%) | -19% (2959, 6%) | -22% (31, 29%) | -33% (105, 36%) |
| sl50_tp50 | -66% (2201, 16%) | -19% (2959, 7%) | -25% (31, 32%) | -34% (105, 36%) |
| no_stop_tp100 | -65% (2201, 14%) | -19% (2959, 6%) | -19% (31, 29%) | -35% (105, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 77499. Outcomes:

- missed_window: 50940
- low_liquidity: 12640
- proven_liquidity_gone: 6322
- no_momentum: 3008
- research_failed: 2213
- proven_low_volume: 1090
- simulated failed buy: 960
- proven_price_collapsed_or_parabolic: 126
- proven: 107
- proven_no_uptrend: 46
- dip: 31
- research_passed: 16

Warning: 621 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
