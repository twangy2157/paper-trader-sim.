# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T21:33:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 12. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2585 | 12% | -66.0% | -68 to -64 | -170869 |
| all momentum | 2601 | 12% | -65.8% | -68 to -64 | -171412 |
| control | 3317 | 6% | -18.6% | -20 to -17 | -61891 |
| dip buy | 34 | 29% | -11.9% | -32 to 8 | -406 |
| proven pools | 113 | 34% | -33.8% | -43 to -24 | -3825 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2580, 12%) | -19% (3317, 6%) | -12% (34, 29%) | -34% (113, 34%) |
| wide_sl50_tp100 | -66% (2580, 13%) | -19% (3317, 6%) | -15% (34, 32%) | -35% (113, 34%) |
| sl30_tp50 | -67% (2580, 14%) | -19% (3317, 7%) | -18% (34, 32%) | -34% (113, 35%) |
| sl50_tp50 | -67% (2580, 15%) | -19% (3317, 7%) | -21% (34, 35%) | -35% (113, 35%) |
| no_stop_tp100 | -66% (2580, 14%) | -19% (3317, 6%) | -13% (34, 32%) | -36% (113, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 89921. Outcomes:

- missed_window: 59006
- low_liquidity: 14770
- proven_liquidity_gone: 7518
- no_momentum: 3365
- research_failed: 2592
- proven_low_volume: 1199
- simulated failed buy: 1112
- proven_price_collapsed_or_parabolic: 138
- proven: 113
- proven_no_uptrend: 57
- dip: 35
- research_passed: 16

Warning: 710 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
