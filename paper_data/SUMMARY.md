# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T03:30:10Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1842 | 12% | -64.7% | -67 to -62 | -119268 |
| all momentum | 1858 | 12% | -64.4% | -67 to -62 | -119812 |
| control | 2621 | 6% | -17.9% | -19 to -17 | -47267 |
| dip buy | 22 | 23% | -19.4% | -45 to 6 | -427 |
| proven pools | 88 | 35% | -28.5% | -39 to -18 | -2514 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1837, 12%) | -18% (2621, 6%) | -19% (22, 23%) | -28% (88, 35%) |
| wide_sl50_tp100 | -65% (1837, 13%) | -18% (2621, 6%) | -23% (22, 27%) | -30% (88, 35%) |
| sl30_tp50 | -66% (1837, 15%) | -18% (2621, 6%) | -28% (22, 23%) | -30% (88, 35%) |
| sl50_tp50 | -66% (1837, 16%) | -18% (2621, 7%) | -32% (22, 27%) | -31% (88, 35%) |
| no_stop_tp100 | -65% (1837, 14%) | -18% (2621, 6%) | -20% (22, 27%) | -31% (88, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 66338. Outcomes:

- missed_window: 43857
- low_liquidity: 10666
- proven_liquidity_gone: 5155
- no_momentum: 2674
- research_failed: 1856
- proven_low_volume: 1017
- simulated failed buy: 831
- proven_price_collapsed_or_parabolic: 116
- proven: 89
- proven_no_uptrend: 39
- dip: 22
- research_passed: 16

Warning: 551 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
