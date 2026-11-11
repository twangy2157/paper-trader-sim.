# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T07:47:30Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1686 | 12% | -64.9% | -68 to -62 | -109558 |
| all momentum | 1702 | 12% | -64.6% | -67 to -62 | -110102 |
| control | 2442 | 5% | -18.0% | -19 to -17 | -44124 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 80 | 36% | -26.2% | -37 to -15 | -2106 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1681, 12%) | -18% (2442, 5%) | -16% (20, 25%) | -26% (80, 36%) |
| wide_sl50_tp100 | -65% (1681, 13%) | -18% (2442, 5%) | -20% (20, 30%) | -28% (80, 36%) |
| sl30_tp50 | -66% (1681, 15%) | -18% (2442, 6%) | -26% (20, 25%) | -27% (80, 36%) |
| sl50_tp50 | -65% (1681, 16%) | -18% (2442, 6%) | -30% (20, 30%) | -29% (80, 36%) |
| no_stop_tp100 | -65% (1681, 14%) | -19% (2442, 5%) | -17% (20, 30%) | -28% (80, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 61097. Outcomes:

- missed_window: 40404
- low_liquidity: 9824
- proven_liquidity_gone: 4665
- no_momentum: 2495
- research_failed: 1697
- proven_low_volume: 967
- simulated failed buy: 785
- proven_price_collapsed_or_parabolic: 105
- proven: 82
- proven_no_uptrend: 37
- dip: 20
- research_passed: 16

Warning: 526 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
