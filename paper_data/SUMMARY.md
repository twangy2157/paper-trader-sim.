# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T09:17:39Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 29. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1895 | 12% | -64.6% | -67 to -62 | -122647 |
| all momentum | 1911 | 12% | -64.4% | -67 to -62 | -123191 |
| control | 2665 | 6% | -18.0% | -19 to -17 | -48270 |
| dip buy | 26 | 27% | -16.9% | -40 to 7 | -440 |
| proven pools | 89 | 35% | -28.6% | -39 to -18 | -2554 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1890, 12%) | -18% (2665, 6%) | -17% (26, 27%) | -29% (89, 35%) |
| wide_sl50_tp100 | -65% (1890, 13%) | -18% (2665, 6%) | -20% (26, 31%) | -30% (89, 35%) |
| sl30_tp50 | -66% (1890, 15%) | -18% (2665, 6%) | -26% (26, 27%) | -30% (89, 35%) |
| sl50_tp50 | -66% (1890, 16%) | -19% (2665, 7%) | -30% (26, 31%) | -31% (89, 35%) |
| no_stop_tp100 | -65% (1890, 14%) | -18% (2665, 6%) | -18% (26, 31%) | -31% (89, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 67701. Outcomes:

- missed_window: 44709
- low_liquidity: 10888
- proven_liquidity_gone: 5312
- no_momentum: 2720
- research_failed: 1910
- proven_low_volume: 1026
- simulated failed buy: 846
- proven_price_collapsed_or_parabolic: 117
- proven: 91
- proven_no_uptrend: 39
- dip: 27
- research_passed: 16

Warning: 560 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
