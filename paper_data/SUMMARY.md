# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T20:04:50Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 19. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2182 | 12% | -64.6% | -67 to -62 | -141157 |
| all momentum | 2198 | 12% | -64.4% | -67 to -62 | -141701 |
| control | 2932 | 6% | -18.2% | -19 to -17 | -53500 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 105 | 35% | -32.6% | -43 to -23 | -3437 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2177, 12%) | -18% (2932, 6%) | -18% (31, 26%) | -33% (105, 35%) |
| wide_sl50_tp100 | -65% (2177, 13%) | -18% (2932, 6%) | -21% (31, 29%) | -34% (105, 35%) |
| sl30_tp50 | -66% (2177, 15%) | -18% (2932, 6%) | -22% (31, 29%) | -33% (105, 36%) |
| sl50_tp50 | -66% (2177, 16%) | -19% (2932, 7%) | -25% (31, 32%) | -34% (105, 36%) |
| no_stop_tp100 | -65% (2177, 14%) | -19% (2932, 6%) | -19% (31, 29%) | -35% (105, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 76589. Outcomes:

- missed_window: 50382
- low_liquidity: 12433
- proven_liquidity_gone: 6235
- no_momentum: 2988
- research_failed: 2189
- proven_low_volume: 1087
- simulated failed buy: 952
- proven_price_collapsed_or_parabolic: 126
- proven: 105
- proven_no_uptrend: 45
- dip: 31
- research_passed: 16

Warning: 618 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
