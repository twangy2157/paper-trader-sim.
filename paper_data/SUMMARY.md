# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T01:36:30Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 4. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2995 | 11% | -66.4% | -68 to -64 | -199051 |
| all momentum | 3012 | 12% | -66.1% | -68 to -64 | -199502 |
| control | 3750 | 6% | -19.2% | -20 to -18 | -72396 |
| dip buy | 38 | 26% | -13.9% | -33 to 5 | -532 |
| proven pools | 117 | 32% | -33.8% | -43 to -24 | -3969 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2991, 12%) | -19% (3750, 6%) | -14% (38, 26%) | -34% (117, 32%) |
| wide_sl50_tp100 | -66% (2991, 13%) | -19% (3750, 6%) | -17% (38, 29%) | -35% (117, 32%) |
| sl30_tp50 | -67% (2991, 14%) | -19% (3750, 7%) | -19% (38, 29%) | -34% (117, 33%) |
| sl50_tp50 | -67% (2991, 15%) | -20% (3750, 7%) | -21% (38, 34%) | -35% (117, 33%) |
| no_stop_tp100 | -66% (2991, 14%) | -20% (3750, 6%) | -15% (38, 29%) | -36% (117, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 100595. Outcomes:

- missed_window: 65480
- low_liquidity: 16704
- proven_liquidity_gone: 8647
- no_momentum: 3794
- research_failed: 2999
- proven_low_volume: 1327
- simulated failed buy: 1261
- proven_price_collapsed_or_parabolic: 152
- proven: 117
- proven_no_uptrend: 59
- dip: 38
- research_passed: 17

Warning: 799 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
