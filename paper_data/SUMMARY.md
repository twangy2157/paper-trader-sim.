# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T20:16:33Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 42.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1784 | 12% | -64.9% | -67 to -62 | -115869 |
| all momentum | 1800 | 12% | -64.6% | -67 to -62 | -116413 |
| control | 2561 | 5% | -18.0% | -19 to -17 | -46390 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 86 | 36% | -28.6% | -40 to -18 | -2469 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1779, 12%) | -18% (2561, 5%) | -20% (21, 24%) | -29% (86, 36%) |
| wide_sl50_tp100 | -65% (1779, 13%) | -18% (2561, 6%) | -24% (21, 29%) | -30% (86, 36%) |
| sl30_tp50 | -66% (1779, 15%) | -18% (2561, 6%) | -29% (21, 24%) | -30% (86, 36%) |
| sl50_tp50 | -66% (1779, 16%) | -18% (2561, 6%) | -33% (21, 29%) | -31% (86, 36%) |
| no_stop_tp100 | -65% (1779, 14%) | -19% (2561, 6%) | -20% (21, 29%) | -30% (86, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 64406. Outcomes:

- missed_window: 42583
- low_liquidity: 10347
- proven_liquidity_gone: 4985
- no_momentum: 2613
- research_failed: 1793
- proven_low_volume: 994
- simulated failed buy: 819
- proven_price_collapsed_or_parabolic: 111
- proven: 87
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 545 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
