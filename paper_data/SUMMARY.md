# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T17:03:11Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2161 | 12% | -64.6% | -67 to -62 | -139701 |
| all momentum | 2177 | 12% | -64.3% | -67 to -62 | -140245 |
| control | 2907 | 6% | -18.1% | -19 to -17 | -52893 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 104 | 35% | -33.2% | -43 to -24 | -3459 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2156, 12%) | -18% (2907, 6%) | -18% (31, 26%) | -33% (104, 35%) |
| wide_sl50_tp100 | -65% (2156, 13%) | -18% (2907, 6%) | -21% (31, 29%) | -35% (104, 35%) |
| sl30_tp50 | -66% (2156, 15%) | -18% (2907, 6%) | -22% (31, 29%) | -33% (104, 36%) |
| sl50_tp50 | -66% (2156, 16%) | -19% (2907, 7%) | -25% (31, 32%) | -34% (104, 36%) |
| no_stop_tp100 | -65% (2156, 14%) | -19% (2907, 6%) | -19% (31, 29%) | -36% (104, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 75870. Outcomes:

- missed_window: 49974
- low_liquidity: 12269
- proven_liquidity_gone: 6153
- no_momentum: 2958
- research_failed: 2171
- proven_low_volume: 1084
- simulated failed buy: 941
- proven_price_collapsed_or_parabolic: 125
- proven: 105
- proven_no_uptrend: 43
- dip: 31
- research_passed: 16

Warning: 614 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
