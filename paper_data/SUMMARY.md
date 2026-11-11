# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T05:19:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 34.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1671 | 12% | -64.8% | -68 to -62 | -108442 |
| all momentum | 1687 | 12% | -64.5% | -67 to -62 | -108986 |
| control | 2418 | 5% | -18.0% | -19 to -17 | -43814 |
| dip buy | 19 | 21% | -21.9% | -46 to 3 | -416 |
| proven pools | 80 | 36% | -26.2% | -37 to -15 | -2106 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1666, 12%) | -18% (2418, 5%) | -22% (19, 21%) | -26% (80, 36%) |
| wide_sl50_tp100 | -65% (1666, 13%) | -18% (2418, 5%) | -26% (19, 26%) | -28% (80, 36%) |
| sl30_tp50 | -66% (1666, 15%) | -18% (2418, 6%) | -30% (19, 21%) | -27% (80, 36%) |
| sl50_tp50 | -65% (1666, 16%) | -19% (2418, 6%) | -33% (19, 26%) | -29% (80, 36%) |
| no_stop_tp100 | -65% (1666, 14%) | -19% (2418, 5%) | -22% (19, 26%) | -28% (80, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 60678. Outcomes:

- missed_window: 40199
- low_liquidity: 9733
- proven_liquidity_gone: 4598
- no_momentum: 2474
- research_failed: 1679
- proven_low_volume: 963
- simulated failed buy: 775
- proven_price_collapsed_or_parabolic: 104
- proven: 80
- proven_no_uptrend: 37
- dip: 20
- research_passed: 16

Warning: 516 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
