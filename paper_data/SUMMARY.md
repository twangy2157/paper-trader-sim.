# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T05:41:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 36.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1674 | 12% | -64.9% | -68 to -62 | -108743 |
| all momentum | 1690 | 12% | -64.6% | -67 to -62 | -109286 |
| control | 2421 | 5% | -18.0% | -19 to -17 | -43741 |
| dip buy | 19 | 21% | -21.9% | -46 to 3 | -416 |
| proven pools | 80 | 36% | -26.2% | -37 to -15 | -2106 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1669, 12%) | -18% (2421, 5%) | -22% (19, 21%) | -26% (80, 36%) |
| wide_sl50_tp100 | -65% (1669, 13%) | -18% (2421, 5%) | -26% (19, 26%) | -28% (80, 36%) |
| sl30_tp50 | -66% (1669, 15%) | -18% (2421, 6%) | -30% (19, 21%) | -27% (80, 36%) |
| sl50_tp50 | -65% (1669, 16%) | -18% (2421, 6%) | -33% (19, 26%) | -29% (80, 36%) |
| no_stop_tp100 | -65% (1669, 14%) | -19% (2421, 5%) | -22% (19, 26%) | -28% (80, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 60743. Outcomes:

- missed_window: 40227
- low_liquidity: 9748
- proven_liquidity_gone: 4610
- no_momentum: 2479
- research_failed: 1680
- proven_low_volume: 964
- simulated failed buy: 777
- proven_price_collapsed_or_parabolic: 105
- proven: 80
- proven_no_uptrend: 37
- dip: 20
- research_passed: 16

Warning: 518 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
