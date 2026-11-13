# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T17:45:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2167 | 12% | -64.6% | -67 to -62 | -140189 |
| all momentum | 2183 | 12% | -64.4% | -67 to -62 | -140733 |
| control | 2914 | 6% | -18.1% | -19 to -17 | -52915 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 105 | 35% | -32.6% | -43 to -23 | -3437 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2162, 12%) | -18% (2914, 6%) | -18% (31, 26%) | -33% (105, 35%) |
| wide_sl50_tp100 | -65% (2162, 13%) | -18% (2914, 6%) | -21% (31, 29%) | -34% (105, 35%) |
| sl30_tp50 | -66% (2162, 15%) | -18% (2914, 6%) | -22% (31, 29%) | -33% (105, 36%) |
| sl50_tp50 | -66% (2162, 16%) | -19% (2914, 7%) | -25% (31, 32%) | -34% (105, 36%) |
| no_stop_tp100 | -65% (2162, 14%) | -19% (2914, 6%) | -19% (31, 29%) | -35% (105, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 76017. Outcomes:

- missed_window: 50052
- low_liquidity: 12307
- proven_liquidity_gone: 6171
- no_momentum: 2965
- research_failed: 2174
- proven_low_volume: 1085
- simulated failed buy: 943
- proven_price_collapsed_or_parabolic: 125
- proven: 105
- proven_no_uptrend: 43
- dip: 31
- research_passed: 16

Warning: 614 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
