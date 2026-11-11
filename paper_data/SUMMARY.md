# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T03:37:29Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 21. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1657 | 12% | -65.0% | -68 to -62 | -107788 |
| all momentum | 1673 | 12% | -64.7% | -67 to -62 | -108332 |
| control | 2406 | 5% | -18.0% | -19 to -17 | -43623 |
| dip buy | 17 | 24% | -20.2% | -47 to 8 | -345 |
| proven pools | 79 | 37% | -26.1% | -37 to -15 | -2066 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1652, 12%) | -18% (2406, 5%) | -20% (17, 24%) | -26% (79, 37%) |
| wide_sl50_tp100 | -65% (1652, 13%) | -18% (2406, 5%) | -26% (17, 24%) | -27% (79, 37%) |
| sl30_tp50 | -66% (1652, 15%) | -18% (2406, 6%) | -29% (17, 24%) | -27% (79, 37%) |
| sl50_tp50 | -65% (1652, 16%) | -19% (2406, 6%) | -34% (17, 24%) | -28% (79, 37%) |
| no_stop_tp100 | -65% (1652, 14%) | -19% (2406, 5%) | -22% (17, 24%) | -27% (79, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 60295. Outcomes:

- missed_window: 39963
- low_liquidity: 9668
- proven_liquidity_gone: 4558
- no_momentum: 2459
- research_failed: 1666
- proven_low_volume: 957
- simulated failed buy: 769
- proven_price_collapsed_or_parabolic: 104
- proven: 80
- proven_no_uptrend: 36
- dip: 19
- research_passed: 16

Warning: 514 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
