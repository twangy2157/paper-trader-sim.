# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T18:10:55Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 35. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2924 | 12% | -66.1% | -68 to -64 | -193640 |
| all momentum | 2941 | 12% | -65.9% | -68 to -64 | -194091 |
| control | 3663 | 6% | -19.2% | -20 to -18 | -70684 |
| dip buy | 38 | 26% | -13.9% | -33 to 5 | -532 |
| proven pools | 116 | 33% | -34.1% | -44 to -24 | -3966 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2920, 12%) | -19% (3663, 6%) | -14% (38, 26%) | -34% (116, 33%) |
| wide_sl50_tp100 | -66% (2920, 13%) | -19% (3663, 6%) | -17% (38, 29%) | -35% (116, 33%) |
| sl30_tp50 | -67% (2920, 14%) | -19% (3663, 7%) | -19% (38, 29%) | -34% (116, 34%) |
| sl50_tp50 | -67% (2920, 15%) | -20% (3663, 7%) | -21% (38, 34%) | -35% (116, 34%) |
| no_stop_tp100 | -66% (2920, 14%) | -20% (3663, 6%) | -15% (38, 29%) | -36% (116, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 99001. Outcomes:

- missed_window: 64532
- low_liquidity: 16417
- proven_liquidity_gone: 8456
- no_momentum: 3728
- research_failed: 2938
- proven_low_volume: 1312
- simulated failed buy: 1238
- proven_price_collapsed_or_parabolic: 150
- proven: 116
- proven_no_uptrend: 59
- dip: 38
- research_passed: 17

Warning: 788 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
