# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-12T20:47:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1996 | 12% | -65.0% | -68 to -63 | -129981 |
| all momentum | 2012 | 12% | -64.8% | -67 to -62 | -130524 |
| control | 2764 | 6% | -17.8% | -19 to -17 | -49543 |
| dip buy | 27 | 26% | -19.9% | -44 to 4 | -539 |
| proven pools | 95 | 35% | -30.4% | -41 to -20 | -2892 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1991, 12%) | -18% (2764, 6%) | -20% (27, 26%) | -30% (95, 35%) |
| wide_sl50_tp100 | -65% (1991, 13%) | -18% (2764, 6%) | -23% (27, 30%) | -32% (95, 35%) |
| sl30_tp50 | -66% (1991, 15%) | -18% (2764, 6%) | -25% (27, 30%) | -30% (95, 36%) |
| sl50_tp50 | -66% (1991, 16%) | -18% (2764, 7%) | -28% (27, 33%) | -32% (95, 36%) |
| no_stop_tp100 | -65% (1991, 14%) | -18% (2764, 6%) | -21% (27, 30%) | -33% (95, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 70516. Outcomes:

- missed_window: 46462
- low_liquidity: 11379
- proven_liquidity_gone: 5620
- no_momentum: 2817
- research_failed: 2003
- proven_low_volume: 1048
- simulated failed buy: 883
- proven_price_collapsed_or_parabolic: 121
- proven: 97
- proven_no_uptrend: 42
- dip: 28
- research_passed: 16

Warning: 582 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
