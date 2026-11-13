# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T15:38:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 15. Pools on watchlist: 74.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2151 | 12% | -64.5% | -67 to -62 | -138982 |
| all momentum | 2167 | 12% | -64.3% | -67 to -62 | -139525 |
| control | 2902 | 6% | -18.0% | -19 to -17 | -52572 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 103 | 35% | -32.5% | -42 to -23 | -3359 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2146, 12%) | -18% (2902, 6%) | -18% (31, 26%) | -33% (103, 35%) |
| wide_sl50_tp100 | -65% (2146, 14%) | -18% (2902, 6%) | -21% (31, 29%) | -34% (103, 35%) |
| sl30_tp50 | -66% (2146, 15%) | -18% (2902, 6%) | -22% (31, 29%) | -32% (103, 36%) |
| sl50_tp50 | -66% (2146, 16%) | -19% (2902, 7%) | -25% (31, 32%) | -34% (103, 36%) |
| no_stop_tp100 | -65% (2146, 14%) | -19% (2902, 6%) | -19% (31, 29%) | -35% (103, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 75476. Outcomes:

- missed_window: 49734
- low_liquidity: 12181
- proven_liquidity_gone: 6111
- no_momentum: 2951
- research_failed: 2159
- proven_low_volume: 1082
- simulated failed buy: 938
- proven_price_collapsed_or_parabolic: 125
- proven: 105
- proven_no_uptrend: 43
- dip: 31
- research_passed: 16

Warning: 611 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
