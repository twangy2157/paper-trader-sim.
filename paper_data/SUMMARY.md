# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T13:10:10Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 13. Pools on watchlist: 24.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2869 | 12% | -66.1% | -68 to -64 | -189819 |
| all momentum | 2886 | 12% | -65.8% | -68 to -64 | -190270 |
| control | 3609 | 6% | -19.1% | -20 to -18 | -69182 |
| dip buy | 37 | 27% | -13.3% | -33 to 5 | -496 |
| proven pools | 116 | 33% | -34.1% | -44 to -24 | -3966 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2865, 12%) | -19% (3609, 6%) | -13% (37, 27%) | -34% (116, 33%) |
| wide_sl50_tp100 | -66% (2865, 13%) | -19% (3609, 6%) | -16% (37, 30%) | -35% (116, 33%) |
| sl30_tp50 | -67% (2865, 14%) | -19% (3609, 7%) | -19% (37, 30%) | -34% (116, 34%) |
| sl50_tp50 | -67% (2865, 15%) | -19% (3609, 7%) | -19% (37, 35%) | -35% (116, 34%) |
| no_stop_tp100 | -66% (2865, 14%) | -20% (3609, 6%) | -13% (37, 30%) | -36% (116, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 97566. Outcomes:

- missed_window: 63748
- low_liquidity: 16075
- proven_liquidity_gone: 8325
- no_momentum: 3656
- research_failed: 2879
- proven_low_volume: 1294
- simulated failed buy: 1211
- proven_price_collapsed_or_parabolic: 149
- proven: 116
- proven_no_uptrend: 59
- dip: 37
- research_passed: 17

Warning: 773 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
