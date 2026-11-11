# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T16:44:31Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 18. Pools on watchlist: 68.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1760 | 12% | -64.9% | -68 to -62 | -114431 |
| all momentum | 1776 | 12% | -64.6% | -67 to -62 | -114975 |
| control | 2524 | 5% | -17.9% | -19 to -17 | -45465 |
| dip buy | 21 | 24% | -20.0% | -47 to 7 | -422 |
| proven pools | 85 | 36% | -27.8% | -38 to -17 | -2368 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1755, 12%) | -18% (2524, 5%) | -20% (21, 24%) | -28% (85, 36%) |
| wide_sl50_tp100 | -65% (1755, 13%) | -18% (2524, 6%) | -24% (21, 29%) | -29% (85, 36%) |
| sl30_tp50 | -66% (1755, 15%) | -18% (2524, 6%) | -29% (21, 24%) | -29% (85, 36%) |
| sl50_tp50 | -66% (1755, 16%) | -18% (2524, 7%) | -33% (21, 29%) | -30% (85, 36%) |
| no_stop_tp100 | -65% (1755, 14%) | -19% (2524, 6%) | -20% (21, 29%) | -29% (85, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 63302. Outcomes:

- missed_window: 41791
- low_liquidity: 10210
- proven_liquidity_gone: 4903
- no_momentum: 2578
- research_failed: 1768
- proven_low_volume: 980
- simulated failed buy: 804
- proven_price_collapsed_or_parabolic: 109
- proven: 85
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 538 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
