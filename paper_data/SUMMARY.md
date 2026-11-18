# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T01:15:11Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 11. Pools on watchlist: 32.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2989 | 11% | -66.3% | -68 to -64 | -198544 |
| all momentum | 3006 | 12% | -66.1% | -68 to -64 | -198994 |
| control | 3746 | 6% | -19.2% | -20 to -18 | -72273 |
| dip buy | 38 | 26% | -13.9% | -33 to 5 | -532 |
| proven pools | 117 | 32% | -33.8% | -43 to -24 | -3969 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2985, 12%) | -19% (3746, 6%) | -14% (38, 26%) | -34% (117, 32%) |
| wide_sl50_tp100 | -66% (2985, 13%) | -19% (3746, 6%) | -17% (38, 29%) | -35% (117, 32%) |
| sl30_tp50 | -67% (2985, 14%) | -19% (3746, 7%) | -19% (38, 29%) | -34% (117, 33%) |
| sl50_tp50 | -67% (2985, 15%) | -20% (3746, 7%) | -21% (38, 34%) | -35% (117, 33%) |
| no_stop_tp100 | -66% (2985, 14%) | -20% (3746, 6%) | -15% (38, 29%) | -36% (117, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 100507. Outcomes:

- missed_window: 65422
- low_liquidity: 16691
- proven_liquidity_gone: 8634
- no_momentum: 3794
- research_failed: 2996
- proven_low_volume: 1326
- simulated failed buy: 1261
- proven_price_collapsed_or_parabolic: 152
- proven: 117
- proven_no_uptrend: 59
- dip: 38
- research_passed: 17

Warning: 799 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
