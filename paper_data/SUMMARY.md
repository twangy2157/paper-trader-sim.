# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T10:42:31Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 17. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2841 | 12% | -66.0% | -68 to -64 | -187896 |
| all momentum | 2858 | 12% | -65.8% | -68 to -64 | -188346 |
| control | 3584 | 6% | -19.1% | -20 to -18 | -68747 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 116 | 33% | -34.1% | -44 to -24 | -3966 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2837, 12%) | -19% (3584, 6%) | -12% (36, 28%) | -34% (116, 33%) |
| wide_sl50_tp100 | -66% (2837, 13%) | -19% (3584, 6%) | -15% (36, 31%) | -35% (116, 33%) |
| sl30_tp50 | -67% (2837, 14%) | -19% (3584, 7%) | -18% (36, 31%) | -34% (116, 34%) |
| sl50_tp50 | -67% (2837, 15%) | -19% (3584, 7%) | -19% (36, 36%) | -35% (116, 34%) |
| no_stop_tp100 | -66% (2837, 14%) | -20% (3584, 6%) | -13% (36, 31%) | -36% (116, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 96994. Outcomes:

- missed_window: 63375
- low_liquidity: 15998
- proven_liquidity_gone: 8273
- no_momentum: 3636
- research_failed: 2850
- proven_low_volume: 1285
- simulated failed buy: 1201
- proven_price_collapsed_or_parabolic: 148
- proven: 116
- proven_no_uptrend: 59
- dip: 36
- research_passed: 17

Warning: 768 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
