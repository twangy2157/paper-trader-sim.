# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T11:35:42Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 26. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2849 | 12% | -66.1% | -68 to -64 | -188546 |
| all momentum | 2866 | 12% | -65.9% | -68 to -64 | -188996 |
| control | 3591 | 6% | -19.1% | -20 to -18 | -68776 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 116 | 33% | -34.1% | -44 to -24 | -3966 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2845, 12%) | -19% (3591, 6%) | -12% (36, 28%) | -34% (116, 33%) |
| wide_sl50_tp100 | -66% (2845, 13%) | -19% (3591, 6%) | -15% (36, 31%) | -35% (116, 33%) |
| sl30_tp50 | -67% (2845, 14%) | -19% (3591, 7%) | -18% (36, 31%) | -34% (116, 34%) |
| sl50_tp50 | -67% (2845, 15%) | -19% (3591, 7%) | -19% (36, 36%) | -35% (116, 34%) |
| no_stop_tp100 | -66% (2845, 14%) | -20% (3591, 6%) | -13% (36, 31%) | -36% (116, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 97195. Outcomes:

- missed_window: 63493
- low_liquidity: 16038
- proven_liquidity_gone: 8284
- no_momentum: 3646
- research_failed: 2864
- proven_low_volume: 1288
- simulated failed buy: 1206
- proven_price_collapsed_or_parabolic: 148
- proven: 116
- proven_no_uptrend: 59
- dip: 36
- research_passed: 17

Warning: 770 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
