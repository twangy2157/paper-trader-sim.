# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-11T15:29:12Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 14. Pools on watchlist: 71.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1752 | 12% | -64.9% | -68 to -62 | -113896 |
| all momentum | 1768 | 12% | -64.6% | -67 to -62 | -114440 |
| control | 2516 | 5% | -17.9% | -19 to -16 | -45150 |
| dip buy | 20 | 25% | -16.1% | -42 to 10 | -323 |
| proven pools | 85 | 36% | -27.8% | -38 to -17 | -2368 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -65% (1747, 12%) | -18% (2516, 5%) | -16% (20, 25%) | -28% (85, 36%) |
| wide_sl50_tp100 | -65% (1747, 13%) | -18% (2516, 6%) | -20% (20, 30%) | -29% (85, 36%) |
| sl30_tp50 | -66% (1747, 15%) | -18% (2516, 6%) | -26% (20, 25%) | -29% (85, 36%) |
| sl50_tp50 | -66% (1747, 16%) | -18% (2516, 7%) | -30% (20, 30%) | -30% (85, 36%) |
| no_stop_tp100 | -65% (1747, 14%) | -18% (2516, 6%) | -17% (20, 30%) | -29% (85, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 62905. Outcomes:

- missed_window: 41526
- low_liquidity: 10142
- proven_liquidity_gone: 4865
- no_momentum: 2566
- research_failed: 1759
- proven_low_volume: 980
- simulated failed buy: 800
- proven_price_collapsed_or_parabolic: 108
- proven: 85
- proven_no_uptrend: 37
- dip: 21
- research_passed: 16

Warning: 536 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
