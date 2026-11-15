# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-15T02:02:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2413 | 12% | -65.4% | -68 to -63 | -158100 |
| all momentum | 2429 | 12% | -65.2% | -67 to -63 | -158644 |
| control | 3146 | 6% | -18.7% | -20 to -17 | -59154 |
| dip buy | 33 | 30% | -12.1% | -32 to 8 | -402 |
| proven pools | 109 | 34% | -34.3% | -44 to -24 | -3744 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2408, 12%) | -19% (3146, 6%) | -12% (33, 30%) | -34% (109, 34%) |
| wide_sl50_tp100 | -65% (2408, 13%) | -19% (3146, 6%) | -15% (33, 33%) | -36% (109, 34%) |
| sl30_tp50 | -67% (2408, 14%) | -19% (3146, 7%) | -18% (33, 33%) | -34% (109, 35%) |
| sl50_tp50 | -66% (2408, 16%) | -19% (3146, 7%) | -21% (33, 36%) | -36% (109, 35%) |
| no_stop_tp100 | -65% (2408, 14%) | -19% (3146, 6%) | -13% (33, 33%) | -36% (109, 34%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 84911. Outcomes:

- missed_window: 55821
- low_liquidity: 13926
- proven_liquidity_gone: 7028
- no_momentum: 3199
- research_failed: 2422
- proven_low_volume: 1137
- simulated failed buy: 1033
- proven_price_collapsed_or_parabolic: 134
- proven: 110
- proven_no_uptrend: 52
- dip: 33
- research_passed: 16

Warning: 655 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
