# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T09:02:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 26. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1700 | 12% | -65.0% | -68 to -62 | -110675 |
| all momentum | 1716 | 12% | -64.7% | -67 to -62 | -111218 |
| control | 2452 | 5% | -17.9% | -19 to -17 | -44190 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 80 | 36% | -26.2% | -37 to -15 | -2106 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1695, 12%) | -18% (2452, 5%) | -16% (20, 25%) | -26% (80, 36%) |
| wide_sl50_tp100 | -65% (1695, 13%) | -18% (2452, 5%) | -20% (20, 30%) | -28% (80, 36%) |
| sl30_tp50 | -66% (1695, 15%) | -18% (2452, 6%) | -26% (20, 25%) | -27% (80, 36%) |
| sl50_tp50 | -66% (1695, 16%) | -18% (2452, 6%) | -30% (20, 30%) | -29% (80, 36%) |
| no_stop_tp100 | -65% (1695, 14%) | -19% (2452, 5%) | -17% (20, 30%) | -28% (80, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 61379. Outcomes:

- missed_window: 40573
- low_liquidity: 9877
- proven_liquidity_gone: 4689
- no_momentum: 2509
- research_failed: 1711
- proven_low_volume: 971
- simulated failed buy: 789
- proven_price_collapsed_or_parabolic: 105
- proven: 82
- proven_no_uptrend: 37
- dip: 20
- research_passed: 16

Warning: 528 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
