# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-14T06:11:54Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 30.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2258 | 12% | -64.6% | -67 to -62 | -146120 |
| all momentum | 2274 | 12% | -64.4% | -67 to -62 | -146664 |
| control | 3005 | 6% | -18.5% | -20 to -17 | -55734 |
| dip buy | 32 | 28% | -15.4% | -37 to 5 | -493 |
| proven pools | 107 | 35% | -33.0% | -43 to -23 | -3544 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2253, 12%) | -18% (3005, 6%) | -15% (32, 28%) | -33% (107, 35%) |
| wide_sl50_tp100 | -65% (2253, 14%) | -19% (3005, 6%) | -18% (32, 31%) | -34% (107, 35%) |
| sl30_tp50 | -66% (2253, 15%) | -19% (3005, 7%) | -20% (32, 31%) | -33% (107, 36%) |
| sl50_tp50 | -66% (2253, 16%) | -19% (3005, 7%) | -23% (32, 34%) | -34% (107, 36%) |
| no_stop_tp100 | -65% (2253, 14%) | -19% (3005, 6%) | -16% (32, 31%) | -35% (107, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 79233. Outcomes:

- missed_window: 51993
- low_liquidity: 12997
- proven_liquidity_gone: 6505
- no_momentum: 3058
- research_failed: 2264
- proven_low_volume: 1105
- simulated failed buy: 981
- proven_price_collapsed_or_parabolic: 128
- proven: 107
- proven_no_uptrend: 47
- dip: 32
- research_passed: 16

Warning: 635 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
