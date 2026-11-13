# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-13T16:09:41Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 9. Pools on watchlist: 28.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 2158 | 12% | -64.5% | -67 to -62 | -139400 |
| all momentum | 2174 | 12% | -64.3% | -67 to -62 | -139943 |
| control | 2905 | 6% | -18.1% | -19 to -17 | -52783 |
| dip buy | 31 | 26% | -18.1% | -40 to 2 | -564 |
| proven pools | 104 | 35% | -33.2% | -43 to -24 | -3459 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (2153, 12%) | -18% (2905, 6%) | -18% (31, 26%) | -33% (104, 35%) |
| wide_sl50_tp100 | -65% (2153, 14%) | -18% (2905, 6%) | -21% (31, 29%) | -35% (104, 35%) |
| sl30_tp50 | -66% (2153, 15%) | -18% (2905, 6%) | -22% (31, 29%) | -33% (104, 36%) |
| sl50_tp50 | -66% (2153, 16%) | -19% (2905, 7%) | -25% (31, 32%) | -34% (104, 36%) |
| no_stop_tp100 | -65% (2153, 14%) | -19% (2905, 6%) | -19% (31, 29%) | -36% (104, 35%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 75664. Outcomes:

- missed_window: 49872
- low_liquidity: 12205
- proven_liquidity_gone: 6129
- no_momentum: 2952
- research_failed: 2163
- proven_low_volume: 1084
- simulated failed buy: 939
- proven_price_collapsed_or_parabolic: 125
- proven: 105
- proven_no_uptrend: 43
- dip: 31
- research_passed: 16

Warning: 612 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
