# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T16:55:55Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 19. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2910 | 12% | -66.1% | -68 to -64 | -192530 |
| all momentum | 2927 | 12% | -65.8% | -68 to -64 | -192981 |
| control | 3653 | 6% | -19.1% | -20 to -18 | -70103 |
| dip buy | 38 | 26% | -13.9% | -33 to 5 | -532 |
| proven pools | 116 | 33% | -34.1% | -44 to -24 | -3966 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2906, 12%) | -19% (3653, 6%) | -14% (38, 26%) | -34% (116, 33%) |
| wide_sl50_tp100 | -66% (2906, 13%) | -19% (3653, 6%) | -17% (38, 29%) | -35% (116, 33%) |
| sl30_tp50 | -67% (2906, 14%) | -19% (3653, 7%) | -19% (38, 29%) | -34% (116, 34%) |
| sl50_tp50 | -67% (2906, 15%) | -20% (3653, 7%) | -21% (38, 34%) | -35% (116, 34%) |
| no_stop_tp100 | -66% (2906, 14%) | -20% (3653, 6%) | -15% (38, 29%) | -36% (116, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 98632. Outcomes:

- missed_window: 64360
- low_liquidity: 16305
- proven_liquidity_gone: 8430
- no_momentum: 3706
- research_failed: 2920
- proven_low_volume: 1305
- simulated failed buy: 1226
- proven_price_collapsed_or_parabolic: 150
- proven: 116
- proven_no_uptrend: 59
- dip: 38
- research_passed: 17

Warning: 781 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
