# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T04:22:43Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 41.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1665 | 12% | -64.9% | -68 to -62 | -108150 |
| all momentum | 1681 | 12% | -64.6% | -67 to -62 | -108694 |
| control | 2413 | 5% | -18.0% | -19 to -17 | -43687 |
| dip buy | 19 | 21% | -21.9% | -46 to 3 | -416 |
| proven pools | 79 | 37% | -26.1% | -37 to -15 | -2066 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1660, 12%) | -18% (2413, 5%) | -22% (19, 21%) | -26% (79, 37%) |
| wide_sl50_tp100 | -65% (1660, 13%) | -18% (2413, 5%) | -26% (19, 26%) | -27% (79, 37%) |
| sl30_tp50 | -66% (1660, 15%) | -18% (2413, 6%) | -30% (19, 21%) | -27% (79, 37%) |
| sl50_tp50 | -65% (1660, 16%) | -18% (2413, 6%) | -33% (19, 26%) | -28% (79, 37%) |
| no_stop_tp100 | -65% (1660, 14%) | -19% (2413, 5%) | -22% (19, 26%) | -27% (79, 37%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 60478. Outcomes:

- missed_window: 40085
- low_liquidity: 9693
- proven_liquidity_gone: 4581
- no_momentum: 2463
- research_failed: 1672
- proven_low_volume: 959
- simulated failed buy: 770
- proven_price_collapsed_or_parabolic: 104
- proven: 80
- proven_no_uptrend: 36
- dip: 19
- research_passed: 16

Warning: 515 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
