# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T15:50:39Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 16. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1755 | 12% | -64.9% | -68 to -62 | -114134 |
| all momentum | 1771 | 12% | -64.7% | -67 to -62 | -114678 |
| control | 2519 | 5% | -17.9% | -19 to -17 | -45251 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 85 | 36% | -27.8% | -38 to -17 | -2368 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1750, 12%) | -18% (2519, 5%) | -16% (20, 25%) | -28% (85, 36%) |
| wide_sl50_tp100 | -65% (1750, 13%) | -18% (2519, 6%) | -20% (20, 30%) | -29% (85, 36%) |
| sl30_tp50 | -66% (1750, 15%) | -18% (2519, 6%) | -26% (20, 25%) | -29% (85, 36%) |
| sl50_tp50 | -66% (1750, 16%) | -18% (2519, 7%) | -30% (20, 30%) | -30% (85, 36%) |
| no_stop_tp100 | -65% (1750, 14%) | -18% (2519, 6%) | -17% (20, 30%) | -29% (85, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 63041. Outcomes:

- missed_window: 41628
- low_liquidity: 10157
- proven_liquidity_gone: 4874
- no_momentum: 2572
- research_failed: 1761
- proven_low_volume: 980
- simulated failed buy: 801
- proven_price_collapsed_or_parabolic: 109
- proven: 85
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 537 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
