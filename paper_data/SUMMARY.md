# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T10:25:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2293 | 12% | -64.9% | -67 to -62 | -148954 |
| all momentum | 2309 | 12% | -64.7% | -67 to -62 | -149497 |
| control | 3036 | 6% | -18.4% | -20 to -17 | -56118 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2288, 12%) | -18% (3036, 6%) | -15% (32, 28%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2288, 13%) | -19% (3036, 6%) | -18% (32, 31%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2288, 15%) | -19% (3036, 7%) | -20% (32, 31%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2288, 16%) | -19% (3036, 7%) | -23% (32, 34%) | -34% (107, 36%) |
| no_stop_tp100 | -65% (2288, 14%) | -19% (3036, 6%) | -16% (32, 31%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 80188. Outcomes:

- missed_window: 52553
- low_liquidity: 13188
- proven_liquidity_gone: 6622
- no_momentum: 3090
- research_failed: 2304
- proven_low_volume: 1111
- simulated failed buy: 988
- proven_price_collapsed_or_parabolic: 130
- proven: 107
- proven_no_uptrend: 47
- dip: 32
- research_passed: 16

Warning: 639 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
