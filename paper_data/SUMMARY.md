# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T08:46:50Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 25. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2816 | 12% | -66.1% | -68 to -64 | -186473 |
| all momentum | 2833 | 12% | -65.9% | -68 to -64 | -186923 |
| control | 3565 | 6% | -19.1% | -20 to -18 | -68277 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 116 | 33% | -34.1% | -44 to -24 | -3966 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2812, 12%) | -19% (3565, 6%) | -12% (36, 28%) | -34% (116, 33%) |
| wide_sl50_tp100 | -66% (2812, 13%) | -19% (3565, 6%) | -15% (36, 31%) | -35% (116, 33%) |
| sl30_tp50 | -67% (2812, 14%) | -19% (3565, 7%) | -18% (36, 31%) | -34% (116, 34%) |
| sl50_tp50 | -67% (2812, 15%) | -19% (3565, 7%) | -19% (36, 36%) | -35% (116, 34%) |
| no_stop_tp100 | -66% (2812, 14%) | -20% (3565, 6%) | -13% (36, 31%) | -36% (116, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 96518. Outcomes:

- missed_window: 63081
- low_liquidity: 15919
- proven_liquidity_gone: 8225
- no_momentum: 3621
- research_failed: 2829
- proven_low_volume: 1275
- simulated failed buy: 1193
- proven_price_collapsed_or_parabolic: 147
- proven: 116
- proven_no_uptrend: 59
- dip: 36
- research_passed: 17

Warning: 760 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
