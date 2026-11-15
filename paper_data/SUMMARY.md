# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T22:36:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 20. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2592 | 12% | -66.1% | -68 to -64 | -171502 |
| all momentum | 2608 | 12% | -65.9% | -68 to -64 | -172046 |
| control | 3321 | 6% | -18.6% | -20 to -17 | -62103 |
| dip buy | 35 | 29% | -12.5% | -31 to 8 | -440 |
| proven pools | 113 | 34% | -33.8% | -43 to -24 | -3825 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2587, 12%) | -19% (3321, 6%) | -13% (35, 29%) | -34% (113, 34%) |
| wide_sl50_tp100 | -66% (2587, 13%) | -19% (3321, 6%) | -15% (35, 31%) | -35% (113, 34%) |
| sl30_tp50 | -67% (2587, 14%) | -19% (3321, 7%) | -18% (35, 31%) | -34% (113, 35%) |
| sl50_tp50 | -67% (2587, 15%) | -19% (3321, 7%) | -19% (35, 37%) | -35% (113, 35%) |
| no_stop_tp100 | -66% (2587, 14%) | -19% (3321, 6%) | -13% (35, 31%) | -36% (113, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 90192. Outcomes:

- missed_window: 59163
- low_liquidity: 14832
- proven_liquidity_gone: 7546
- no_momentum: 3378
- research_failed: 2599
- proven_low_volume: 1201
- simulated failed buy: 1113
- proven_price_collapsed_or_parabolic: 138
- proven: 113
- proven_no_uptrend: 58
- dip: 35
- research_passed: 16

Warning: 711 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
