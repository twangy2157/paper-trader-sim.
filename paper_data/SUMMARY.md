# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T14:57:38Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 25. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2887 | 12% | -66.1% | -68 to -64 | -191131 |
| all momentum | 2904 | 12% | -65.9% | -68 to -64 | -191581 |
| control | 3621 | 6% | -19.1% | -20 to -18 | -69458 |
| dip buy | 37 | 27% | -13.3% | -33 to 5 | -496 |
| proven pools | 116 | 33% | -34.1% | -44 to -24 | -3966 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2883, 12%) | -19% (3621, 6%) | -13% (37, 27%) | -34% (116, 33%) |
| wide_sl50_tp100 | -66% (2883, 13%) | -19% (3621, 6%) | -16% (37, 30%) | -35% (116, 33%) |
| sl30_tp50 | -67% (2883, 14%) | -19% (3621, 7%) | -19% (37, 30%) | -34% (116, 34%) |
| sl50_tp50 | -67% (2883, 15%) | -20% (3621, 7%) | -19% (37, 35%) | -35% (116, 34%) |
| no_stop_tp100 | -66% (2883, 14%) | -20% (3621, 6%) | -13% (37, 30%) | -36% (116, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 98045. Outcomes:

- missed_window: 64040
- low_liquidity: 16156
- proven_liquidity_gone: 8373
- no_momentum: 3677
- research_failed: 2899
- proven_low_volume: 1302
- simulated failed buy: 1218
- proven_price_collapsed_or_parabolic: 150
- proven: 116
- proven_no_uptrend: 59
- dip: 38
- research_passed: 17

Warning: 777 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
