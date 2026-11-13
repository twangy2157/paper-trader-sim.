# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T15:48:57Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 104.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2153 | 12% | -64.6% | -67 to -62 | -139182 |
| all momentum | 2169 | 12% | -64.3% | -67 to -62 | -139725 |
| control | 2902 | 6% | -18.0% | -19 to -17 | -52573 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 104 | 35% | -33.2% | -43 to -24 | -3459 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2148, 12%) | -18% (2902, 6%) | -18% (31, 26%) | -33% (104, 35%) |
| wide_sl50_tp100 | -65% (2148, 14%) | -18% (2902, 6%) | -21% (31, 29%) | -35% (104, 35%) |
| sl30_tp50 | -66% (2148, 15%) | -18% (2902, 6%) | -22% (31, 29%) | -33% (104, 36%) |
| sl50_tp50 | -66% (2148, 16%) | -19% (2902, 7%) | -25% (31, 32%) | -34% (104, 36%) |
| no_stop_tp100 | -65% (2148, 14%) | -19% (2902, 6%) | -19% (31, 29%) | -36% (104, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 75516. Outcomes:

- missed_window: 49755
- low_liquidity: 12190
- proven_liquidity_gone: 6116
- no_momentum: 2951
- research_failed: 2161
- proven_low_volume: 1084
- simulated failed buy: 939
- proven_price_collapsed_or_parabolic: 125
- proven: 105
- proven_no_uptrend: 43
- dip: 31
- research_passed: 16

Warning: 612 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
