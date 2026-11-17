# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T04:52:14Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 18. Pools on watchlist: 27.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2791 | 12% | -66.2% | -68 to -64 | -184899 |
| all momentum | 2808 | 12% | -65.9% | -68 to -64 | -185350 |
| control | 3528 | 6% | -19.0% | -20 to -18 | -67403 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 115 | 33% | -34.2% | -44 to -25 | -3949 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2787, 12%) | -19% (3528, 6%) | -12% (36, 28%) | -34% (115, 33%) |
| wide_sl50_tp100 | -66% (2787, 13%) | -19% (3528, 6%) | -15% (36, 31%) | -36% (115, 33%) |
| sl30_tp50 | -67% (2787, 14%) | -19% (3528, 7%) | -18% (36, 31%) | -34% (115, 34%) |
| sl50_tp50 | -67% (2787, 16%) | -19% (3528, 7%) | -19% (36, 36%) | -35% (115, 34%) |
| no_stop_tp100 | -66% (2787, 14%) | -20% (3528, 6%) | -13% (36, 31%) | -36% (115, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 95723. Outcomes:

- missed_window: 62603
- low_liquidity: 15794
- proven_liquidity_gone: 8132
- no_momentum: 3585
- research_failed: 2795
- proven_low_volume: 1259
- simulated failed buy: 1181
- proven_price_collapsed_or_parabolic: 147
- proven: 116
- proven_no_uptrend: 58
- dip: 36
- research_passed: 17

Warning: 752 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
