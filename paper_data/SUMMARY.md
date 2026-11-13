# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T18:18:15Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2172 | 12% | -64.6% | -67 to -62 | -140405 |
| all momentum | 2188 | 12% | -64.3% | -67 to -62 | -140948 |
| control | 2916 | 6% | -18.1% | -19 to -17 | -53030 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 105 | 35% | -32.6% | -43 to -23 | -3437 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2167, 12%) | -18% (2916, 6%) | -18% (31, 26%) | -33% (105, 35%) |
| wide_sl50_tp100 | -65% (2167, 13%) | -18% (2916, 6%) | -21% (31, 29%) | -34% (105, 35%) |
| sl30_tp50 | -66% (2167, 15%) | -18% (2916, 6%) | -22% (31, 29%) | -33% (105, 36%) |
| sl50_tp50 | -66% (2167, 16%) | -19% (2916, 7%) | -25% (31, 32%) | -34% (105, 36%) |
| no_stop_tp100 | -65% (2167, 14%) | -19% (2916, 6%) | -19% (31, 29%) | -35% (105, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 76138. Outcomes:

- missed_window: 50118
- low_liquidity: 12333
- proven_liquidity_gone: 6190
- no_momentum: 2970
- research_failed: 2177
- proven_low_volume: 1085
- simulated failed buy: 945
- proven_price_collapsed_or_parabolic: 125
- proven: 105
- proven_no_uptrend: 43
- dip: 31
- research_passed: 16

Warning: 615 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
