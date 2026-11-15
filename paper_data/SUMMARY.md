# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T22:14:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 11. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2591 | 12% | -66.1% | -68 to -64 | -171401 |
| all momentum | 2607 | 12% | -65.9% | -68 to -64 | -171945 |
| control | 3321 | 6% | -18.6% | -20 to -17 | -62103 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 113 | 34% | -33.8% | -43 to -24 | -3825 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2586, 12%) | -19% (3321, 6%) | -13% (35, 29%) | -34% (113, 34%) |
| wide_sl50_tp100 | -66% (2586, 13%) | -19% (3321, 6%) | -15% (35, 31%) | -35% (113, 34%) |
| sl30_tp50 | -67% (2586, 14%) | -19% (3321, 7%) | -18% (35, 31%) | -34% (113, 35%) |
| sl50_tp50 | -67% (2586, 15%) | -19% (3321, 7%) | -19% (35, 37%) | -35% (113, 35%) |
| no_stop_tp100 | -66% (2586, 14%) | -19% (3321, 6%) | -13% (35, 31%) | -36% (113, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 90102. Outcomes:

- missed_window: 59115
- low_liquidity: 14807
- proven_liquidity_gone: 7540
- no_momentum: 3373
- research_failed: 2594
- proven_low_volume: 1201
- simulated failed buy: 1112
- proven_price_collapsed_or_parabolic: 138
- proven: 113
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 710 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
