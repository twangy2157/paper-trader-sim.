# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T08:56:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 30. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1889 | 12% | -64.6% | -67 to -62 | -122238 |
| all momentum | 1905 | 12% | -64.4% | -67 to -62 | -122781 |
| control | 2662 | 6% | -18.0% | -19 to -17 | -48062 |
| dip buy | 26 | 27% | -16.9% | -40 to 7 | -440 |
| proven pools | 89 | 35% | -28.6% | -39 to -18 | -2554 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1884, 12%) | -18% (2662, 6%) | -17% (26, 27%) | -29% (89, 35%) |
| wide_sl50_tp100 | -65% (1884, 13%) | -18% (2662, 6%) | -20% (26, 31%) | -30% (89, 35%) |
| sl30_tp50 | -66% (1884, 15%) | -18% (2662, 6%) | -26% (26, 27%) | -30% (89, 35%) |
| sl50_tp50 | -66% (1884, 16%) | -18% (2662, 7%) | -30% (26, 31%) | -31% (89, 35%) |
| no_stop_tp100 | -65% (1884, 14%) | -18% (2662, 6%) | -18% (26, 31%) | -31% (89, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 67624. Outcomes:

- missed_window: 44661
- low_liquidity: 10874
- proven_liquidity_gone: 5307
- no_momentum: 2716
- research_failed: 1906
- proven_low_volume: 1025
- simulated failed buy: 845
- proven_price_collapsed_or_parabolic: 117
- proven: 91
- proven_no_uptrend: 39
- dip: 27
- research_passed: 16

Warning: 560 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
