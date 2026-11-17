# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T04:30:36Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 11. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2790 | 12% | -66.1% | -68 to -64 | -184798 |
| all momentum | 2807 | 12% | -65.9% | -68 to -64 | -185249 |
| control | 3526 | 6% | -19.0% | -20 to -18 | -67295 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 115 | 33% | -34.2% | -44 to -25 | -3949 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2786, 12%) | -19% (3526, 6%) | -12% (36, 28%) | -34% (115, 33%) |
| wide_sl50_tp100 | -66% (2786, 13%) | -19% (3526, 6%) | -15% (36, 31%) | -36% (115, 33%) |
| sl30_tp50 | -67% (2786, 14%) | -19% (3526, 7%) | -18% (36, 31%) | -34% (115, 34%) |
| sl50_tp50 | -67% (2786, 16%) | -19% (3526, 7%) | -19% (36, 36%) | -35% (115, 34%) |
| no_stop_tp100 | -66% (2786, 14%) | -19% (3526, 6%) | -13% (36, 31%) | -36% (115, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 95656. Outcomes:

- missed_window: 62577
- low_liquidity: 15776
- proven_liquidity_gone: 8120
- no_momentum: 3578
- research_failed: 2792
- proven_low_volume: 1259
- simulated failed buy: 1180
- proven_price_collapsed_or_parabolic: 147
- proven: 116
- proven_no_uptrend: 58
- dip: 36
- research_passed: 17

Warning: 752 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
