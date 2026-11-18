# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T03:31:43Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 23. Pools on watchlist: 55.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3011 | 11% | -66.4% | -69 to -65 | -200317 |
| all momentum | 3028 | 11% | -66.2% | -68 to -64 | -200767 |
| control | 3757 | 6% | -19.2% | -20 to -18 | -72442 |
| dip buy | 39 | 26% | -13.9% | -32 to 5 | -543 |
| proven pools | 117 | 32% | -33.8% | -43 to -24 | -3969 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3007, 12%) | -19% (3757, 6%) | -14% (39, 26%) | -34% (117, 32%) |
| wide_sl50_tp100 | -66% (3007, 13%) | -19% (3757, 6%) | -17% (39, 28%) | -35% (117, 32%) |
| sl30_tp50 | -67% (3007, 14%) | -19% (3757, 7%) | -19% (39, 28%) | -34% (117, 33%) |
| sl50_tp50 | -67% (3007, 15%) | -20% (3757, 7%) | -21% (39, 33%) | -35% (117, 33%) |
| no_stop_tp100 | -66% (3007, 13%) | -20% (3757, 6%) | -15% (39, 28%) | -36% (117, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 101048. Outcomes:

- missed_window: 65733
- low_liquidity: 16804
- proven_liquidity_gone: 8696
- no_momentum: 3808
- research_failed: 3025
- proven_low_volume: 1330
- simulated failed buy: 1265
- proven_price_collapsed_or_parabolic: 153
- proven: 119
- proven_no_uptrend: 59
- dip: 39
- research_passed: 17

Warning: 801 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
