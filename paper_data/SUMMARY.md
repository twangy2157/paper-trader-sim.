# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T21:00:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2581 | 12% | -66.0% | -68 to -64 | -170468 |
| all momentum | 2597 | 12% | -65.8% | -68 to -63 | -171011 |
| control | 3310 | 6% | -18.6% | -20 to -17 | -61839 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 113 | 34% | -33.8% | -43 to -24 | -3825 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2576, 12%) | -19% (3310, 6%) | -12% (34, 29%) | -34% (113, 34%) |
| wide_sl50_tp100 | -66% (2576, 13%) | -19% (3310, 6%) | -15% (34, 32%) | -35% (113, 34%) |
| sl30_tp50 | -67% (2576, 14%) | -19% (3310, 7%) | -18% (34, 32%) | -34% (113, 35%) |
| sl50_tp50 | -67% (2576, 15%) | -19% (3310, 7%) | -21% (34, 35%) | -35% (113, 35%) |
| no_stop_tp100 | -66% (2576, 14%) | -19% (3310, 6%) | -13% (34, 32%) | -36% (113, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 89801. Outcomes:

- missed_window: 58938
- low_liquidity: 14739
- proven_liquidity_gone: 7502
- no_momentum: 3365
- research_failed: 2590
- proven_low_volume: 1198
- simulated failed buy: 1110
- proven_price_collapsed_or_parabolic: 138
- proven: 113
- proven_no_uptrend: 57
- dip: 35
- research_passed: 16

Warning: 708 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
