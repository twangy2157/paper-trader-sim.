# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T06:02:09Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 31.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1678 | 12% | -65.0% | -68 to -62 | -109143 |
| all momentum | 1694 | 12% | -64.7% | -67 to -62 | -109686 |
| control | 2426 | 5% | -17.9% | -19 to -17 | -43758 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 80 | 36% | -26.2% | -37 to -15 | -2106 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1673, 12%) | -18% (2426, 5%) | -16% (20, 25%) | -26% (80, 36%) |
| wide_sl50_tp100 | -65% (1673, 13%) | -18% (2426, 5%) | -20% (20, 30%) | -28% (80, 36%) |
| sl30_tp50 | -66% (1673, 15%) | -18% (2426, 6%) | -26% (20, 25%) | -27% (80, 36%) |
| sl50_tp50 | -65% (1673, 16%) | -18% (2426, 6%) | -30% (20, 30%) | -29% (80, 36%) |
| no_stop_tp100 | -65% (1673, 14%) | -19% (2426, 5%) | -17% (20, 30%) | -28% (80, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 60809. Outcomes:

- missed_window: 40269
- low_liquidity: 9756
- proven_liquidity_gone: 4620
- no_momentum: 2481
- research_failed: 1683
- proven_low_volume: 965
- simulated failed buy: 777
- proven_price_collapsed_or_parabolic: 105
- proven: 80
- proven_no_uptrend: 37
- dip: 20
- research_passed: 16

Warning: 519 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
