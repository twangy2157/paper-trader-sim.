# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-18T05:16:40Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 28. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3032 | 11% | -66.4% | -68 to -64 | -201738 |
| all momentum | 3049 | 12% | -66.2% | -68 to -64 | -202188 |
| control | 3769 | 6% | -19.2% | -20 to -18 | -72593 |
| dip buy | 40 | 25% | -14.5% | -31 to 3 | -583 |
| proven pools | 117 | 32% | -33.8% | -43 to -24 | -3969 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3028, 12%) | -19% (3769, 6%) | -15% (40, 25%) | -34% (117, 32%) |
| wide_sl50_tp100 | -66% (3028, 13%) | -19% (3769, 6%) | -17% (40, 28%) | -35% (117, 32%) |
| sl30_tp50 | -68% (3028, 14%) | -19% (3769, 7%) | -19% (40, 28%) | -34% (117, 33%) |
| sl50_tp50 | -67% (3028, 15%) | -20% (3769, 7%) | -21% (40, 32%) | -35% (117, 33%) |
| no_stop_tp100 | -66% (3028, 13%) | -20% (3769, 6%) | -15% (40, 28%) | -36% (117, 32%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 101461. Outcomes:

- missed_window: 65989
- low_liquidity: 16867
- proven_liquidity_gone: 8742
- no_momentum: 3823
- research_failed: 3048
- proven_low_volume: 1334
- simulated failed buy: 1270
- proven_price_collapsed_or_parabolic: 153
- proven: 119
- proven_no_uptrend: 59
- dip: 40
- research_passed: 17

Warning: 802 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
