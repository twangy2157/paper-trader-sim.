# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T02:28:51Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 23. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2996 | 11% | -66.4% | -68 to -64 | -199151 |
| all momentum | 3013 | 12% | -66.2% | -68 to -64 | -199602 |
| control | 3750 | 6% | -19.2% | -20 to -18 | -72397 |
| dip buy | 38 | 26% | -13.9% | -33 to 5 | -532 |
| proven pools | 117 | 32% | -33.8% | -43 to -24 | -3969 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2992, 12%) | -19% (3750, 6%) | -14% (38, 26%) | -34% (117, 32%) |
| wide_sl50_tp100 | -66% (2992, 13%) | -19% (3750, 6%) | -17% (38, 29%) | -35% (117, 32%) |
| sl30_tp50 | -67% (2992, 14%) | -19% (3750, 7%) | -19% (38, 29%) | -34% (117, 33%) |
| sl50_tp50 | -67% (2992, 15%) | -20% (3750, 7%) | -21% (38, 34%) | -35% (117, 33%) |
| no_stop_tp100 | -66% (2992, 14%) | -20% (3750, 6%) | -15% (38, 29%) | -36% (117, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 100789. Outcomes:

- missed_window: 65561
- low_liquidity: 16759
- proven_liquidity_gone: 8679
- no_momentum: 3801
- research_failed: 3011
- proven_low_volume: 1330
- simulated failed buy: 1264
- proven_price_collapsed_or_parabolic: 152
- proven: 117
- proven_no_uptrend: 59
- dip: 39
- research_passed: 17

Warning: 801 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
