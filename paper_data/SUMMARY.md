# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T13:57:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2323 | 12% | -65.0% | -67 to -63 | -151189 |
| all momentum | 2339 | 12% | -64.8% | -67 to -63 | -151732 |
| control | 3068 | 6% | -18.4% | -20 to -17 | -56725 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2318, 12%) | -18% (3068, 6%) | -15% (32, 28%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2318, 13%) | -19% (3068, 6%) | -18% (32, 31%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2318, 15%) | -19% (3068, 7%) | -20% (32, 31%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2318, 16%) | -19% (3068, 7%) | -23% (32, 34%) | -34% (107, 36%) |
| no_stop_tp100 | -65% (2318, 14%) | -19% (3068, 6%) | -16% (32, 31%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 81085. Outcomes:

- missed_window: 53130
- low_liquidity: 13343
- proven_liquidity_gone: 6704
- no_momentum: 3117
- research_failed: 2334
- proven_low_volume: 1120
- simulated failed buy: 1000
- proven_price_collapsed_or_parabolic: 131
- proven: 108
- proven_no_uptrend: 50
- dip: 32
- research_passed: 16

Warning: 646 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
