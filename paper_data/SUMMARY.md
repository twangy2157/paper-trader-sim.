# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T03:21:11Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 22. Pools on watchlist: 63.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3009 | 11% | -66.4% | -68 to -64 | -200208 |
| all momentum | 3026 | 12% | -66.2% | -68 to -64 | -200659 |
| control | 3756 | 6% | -19.2% | -20 to -18 | -72434 |
| dip buy | 39 | 26% | -13.9% | -32 to 5 | -543 |
| proven pools | 117 | 32% | -33.8% | -43 to -24 | -3969 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3005, 12%) | -19% (3756, 6%) | -14% (39, 26%) | -34% (117, 32%) |
| wide_sl50_tp100 | -66% (3005, 13%) | -19% (3756, 6%) | -17% (39, 28%) | -35% (117, 32%) |
| sl30_tp50 | -68% (3005, 14%) | -19% (3756, 7%) | -19% (39, 28%) | -34% (117, 33%) |
| sl50_tp50 | -67% (3005, 15%) | -20% (3756, 7%) | -21% (39, 33%) | -35% (117, 33%) |
| no_stop_tp100 | -66% (3005, 13%) | -20% (3756, 6%) | -15% (39, 28%) | -36% (117, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 100994. Outcomes:

- missed_window: 65695
- low_liquidity: 16796
- proven_liquidity_gone: 8692
- no_momentum: 3807
- research_failed: 3024
- proven_low_volume: 1330
- simulated failed buy: 1265
- proven_price_collapsed_or_parabolic: 153
- proven: 117
- proven_no_uptrend: 59
- dip: 39
- research_passed: 17

Warning: 801 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
