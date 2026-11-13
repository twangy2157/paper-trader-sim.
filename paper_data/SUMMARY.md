# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T19:43:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 17. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2180 | 12% | -64.7% | -67 to -62 | -141144 |
| all momentum | 2196 | 12% | -64.4% | -67 to -62 | -141688 |
| control | 2930 | 6% | -18.2% | -19 to -17 | -53481 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 105 | 35% | -32.6% | -43 to -23 | -3437 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2175, 12%) | -18% (2930, 6%) | -18% (31, 26%) | -33% (105, 35%) |
| wide_sl50_tp100 | -65% (2175, 13%) | -18% (2930, 6%) | -21% (31, 29%) | -34% (105, 35%) |
| sl30_tp50 | -66% (2175, 15%) | -19% (2930, 6%) | -22% (31, 29%) | -33% (105, 36%) |
| sl50_tp50 | -66% (2175, 16%) | -19% (2930, 7%) | -25% (31, 32%) | -34% (105, 36%) |
| no_stop_tp100 | -65% (2175, 14%) | -19% (2930, 6%) | -19% (31, 29%) | -35% (105, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 76510. Outcomes:

- missed_window: 50347
- low_liquidity: 12410
- proven_liquidity_gone: 6224
- no_momentum: 2985
- research_failed: 2186
- proven_low_volume: 1086
- simulated failed buy: 950
- proven_price_collapsed_or_parabolic: 126
- proven: 105
- proven_no_uptrend: 44
- dip: 31
- research_passed: 16

Warning: 617 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
