# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T07:19:25Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 10. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1883 | 12% | -64.6% | -67 to -62 | -121853 |
| all momentum | 1899 | 12% | -64.4% | -67 to -62 | -122397 |
| control | 2655 | 6% | -18.0% | -19 to -17 | -47907 |
| dip buy | 25 | 24% | -20.0% | -43 to 4 | -502 |
| proven pools | 89 | 35% | -28.6% | -39 to -18 | -2554 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1878, 12%) | -18% (2655, 6%) | -20% (25, 24%) | -29% (89, 35%) |
| wide_sl50_tp100 | -65% (1878, 13%) | -18% (2655, 6%) | -23% (25, 28%) | -30% (89, 35%) |
| sl30_tp50 | -66% (1878, 15%) | -18% (2655, 6%) | -29% (25, 24%) | -30% (89, 35%) |
| sl50_tp50 | -66% (1878, 16%) | -18% (2655, 7%) | -32% (25, 28%) | -31% (89, 35%) |
| no_stop_tp100 | -65% (1878, 14%) | -18% (2655, 6%) | -21% (25, 28%) | -31% (89, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 67247. Outcomes:

- missed_window: 44461
- low_liquidity: 10788
- proven_liquidity_gone: 5258
- no_momentum: 2703
- research_failed: 1887
- proven_low_volume: 1023
- simulated failed buy: 840
- proven_price_collapsed_or_parabolic: 116
- proven: 91
- proven_no_uptrend: 39
- dip: 25
- research_passed: 16

Warning: 557 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
