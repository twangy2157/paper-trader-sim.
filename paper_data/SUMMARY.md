# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T05:51:38Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 34.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1675 | 12% | -64.9% | -68 to -62 | -108843 |
| all momentum | 1691 | 12% | -64.6% | -67 to -62 | -109386 |
| control | 2422 | 5% | -18.0% | -19 to -17 | -43748 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 80 | 36% | -26.2% | -37 to -15 | -2106 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1670, 12%) | -18% (2422, 5%) | -16% (20, 25%) | -26% (80, 36%) |
| wide_sl50_tp100 | -65% (1670, 13%) | -18% (2422, 5%) | -20% (20, 30%) | -28% (80, 36%) |
| sl30_tp50 | -66% (1670, 15%) | -18% (2422, 6%) | -26% (20, 25%) | -27% (80, 36%) |
| sl50_tp50 | -65% (1670, 16%) | -18% (2422, 6%) | -30% (20, 30%) | -29% (80, 36%) |
| no_stop_tp100 | -65% (1670, 14%) | -19% (2422, 5%) | -17% (20, 30%) | -28% (80, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 60775. Outcomes:

- missed_window: 40242
- low_liquidity: 9754
- proven_liquidity_gone: 4615
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
