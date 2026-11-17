# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T15:28:54Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 29. Pools on watchlist: 49.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2892 | 12% | -66.2% | -68 to -64 | -191631 |
| all momentum | 2909 | 12% | -65.9% | -68 to -64 | -192082 |
| control | 3629 | 6% | -19.1% | -20 to -18 | -69517 |
| dip buy | 38 | 26% | -13.9% | -33 to 5 | -532 |
| proven pools | 116 | 33% | -34.1% | -44 to -24 | -3966 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2888, 12%) | -19% (3629, 6%) | -14% (38, 26%) | -34% (116, 33%) |
| wide_sl50_tp100 | -66% (2888, 13%) | -19% (3629, 6%) | -17% (38, 29%) | -35% (116, 33%) |
| sl30_tp50 | -67% (2888, 14%) | -19% (3629, 7%) | -19% (38, 29%) | -34% (116, 34%) |
| sl50_tp50 | -67% (2888, 15%) | -19% (3629, 7%) | -21% (38, 34%) | -35% (116, 34%) |
| no_stop_tp100 | -66% (2888, 14%) | -20% (3629, 6%) | -15% (38, 29%) | -36% (116, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 98165. Outcomes:

- missed_window: 64087
- low_liquidity: 16199
- proven_liquidity_gone: 8382
- no_momentum: 3690
- research_failed: 2904
- proven_low_volume: 1303
- simulated failed buy: 1220
- proven_price_collapsed_or_parabolic: 150
- proven: 116
- proven_no_uptrend: 59
- dip: 38
- research_passed: 17

Warning: 778 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
