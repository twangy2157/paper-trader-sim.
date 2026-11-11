# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T02:33:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1650 | 12% | -65.0% | -68 to -62 | -107407 |
| all momentum | 1666 | 12% | -64.7% | -67 to -62 | -107950 |
| control | 2393 | 5% | -18.0% | -19 to -17 | -43366 |
| dip buy | 17 | 24% | -20.2% | -47 to 8 | -345 |
| proven pools | 79 | 37% | -26.1% | -37 to -15 | -2066 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1645, 12%) | -18% (2393, 5%) | -20% (17, 24%) | -26% (79, 37%) |
| wide_sl50_tp100 | -65% (1645, 13%) | -18% (2393, 5%) | -26% (17, 24%) | -27% (79, 37%) |
| sl30_tp50 | -66% (1645, 15%) | -18% (2393, 6%) | -29% (17, 24%) | -27% (79, 37%) |
| sl50_tp50 | -66% (1645, 16%) | -19% (2393, 6%) | -34% (17, 24%) | -28% (79, 37%) |
| no_stop_tp100 | -65% (1645, 14%) | -19% (2393, 5%) | -22% (17, 24%) | -27% (79, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 59999. Outcomes:

- missed_window: 39769
- low_liquidity: 9613
- proven_liquidity_gone: 4535
- no_momentum: 2450
- research_failed: 1657
- proven_low_volume: 955
- simulated failed buy: 768
- proven_price_collapsed_or_parabolic: 103
- proven: 80
- proven_no_uptrend: 36
- dip: 17
- research_passed: 16

Warning: 514 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
