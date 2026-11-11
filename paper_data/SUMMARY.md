# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T22:44:40Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 23. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1806 | 12% | -64.9% | -67 to -62 | -117373 |
| all momentum | 1822 | 12% | -64.6% | -67 to -62 | -117917 |
| control | 2579 | 5% | -18.0% | -19 to -17 | -46635 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 87 | 36% | -28.3% | -39 to -18 | -2474 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1801, 12%) | -18% (2579, 5%) | -20% (21, 24%) | -28% (87, 36%) |
| wide_sl50_tp100 | -65% (1801, 13%) | -18% (2579, 6%) | -24% (21, 29%) | -30% (87, 36%) |
| sl30_tp50 | -66% (1801, 15%) | -18% (2579, 6%) | -29% (21, 24%) | -29% (87, 36%) |
| sl50_tp50 | -66% (1801, 16%) | -18% (2579, 6%) | -33% (21, 29%) | -31% (87, 36%) |
| no_stop_tp100 | -65% (1801, 14%) | -19% (2579, 6%) | -20% (21, 29%) | -30% (87, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 65080. Outcomes:

- missed_window: 43010
- low_liquidity: 10471
- proven_liquidity_gone: 5047
- no_momentum: 2637
- research_failed: 1814
- proven_low_volume: 1003
- simulated failed buy: 822
- proven_price_collapsed_or_parabolic: 114
- proven: 88
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 547 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
