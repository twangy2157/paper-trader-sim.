# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T14:23:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 24. Pools on watchlist: 30.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2138 | 12% | -64.4% | -67 to -62 | -137939 |
| all momentum | 2154 | 12% | -64.2% | -67 to -62 | -138483 |
| control | 2888 | 6% | -18.1% | -19 to -17 | -52454 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 103 | 35% | -32.5% | -42 to -23 | -3359 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -64% (2133, 12%) | -18% (2888, 6%) | -18% (31, 26%) | -33% (103, 35%) |
| wide_sl50_tp100 | -65% (2133, 14%) | -18% (2888, 6%) | -21% (31, 29%) | -34% (103, 35%) |
| sl30_tp50 | -66% (2133, 15%) | -18% (2888, 7%) | -22% (31, 29%) | -32% (103, 36%) |
| sl50_tp50 | -66% (2133, 16%) | -19% (2888, 7%) | -25% (31, 32%) | -34% (103, 36%) |
| no_stop_tp100 | -65% (2133, 14%) | -19% (2888, 6%) | -19% (31, 29%) | -35% (103, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 75105. Outcomes:

- missed_window: 49473
- low_liquidity: 12122
- proven_liquidity_gone: 6083
- no_momentum: 2944
- research_failed: 2149
- proven_low_volume: 1078
- simulated failed buy: 937
- proven_price_collapsed_or_parabolic: 125
- proven: 104
- proven_no_uptrend: 43
- dip: 31
- research_passed: 16

Warning: 611 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
