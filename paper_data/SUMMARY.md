# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-17T03:59:10Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 17. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 2784 | 12% | -66.2% | -68 to -64 | -184666 |
| all momentum | 2801 | 12% | -66.0% | -68 to -64 | -185116 |
| control | 3522 | 6% | -19.0% | -20 to -18 | -67250 |
| dip buy | 36 | 28% | -12.3% | -32 to 7 | -446 |
| proven pools | 114 | 33% | -34.3% | -43 to -25 | -3925 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (2780, 12%) | -19% (3522, 6%) | -12% (36, 28%) | -34% (114, 33%) |
| wide_sl50_tp100 | -66% (2780, 13%) | -19% (3522, 6%) | -15% (36, 31%) | -36% (114, 33%) |
| sl30_tp50 | -67% (2780, 14%) | -19% (3522, 7%) | -18% (36, 31%) | -34% (114, 34%) |
| sl50_tp50 | -67% (2780, 15%) | -19% (3522, 7%) | -19% (36, 36%) | -36% (114, 34%) |
| no_stop_tp100 | -66% (2780, 14%) | -19% (3522, 6%) | -13% (36, 31%) | -36% (114, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 95523. Outcomes:

- missed_window: 62486
- low_liquidity: 15757
- proven_liquidity_gone: 8104
- no_momentum: 3574
- research_failed: 2791
- proven_low_volume: 1257
- simulated failed buy: 1180
- proven_price_collapsed_or_parabolic: 147
- proven: 116
- proven_no_uptrend: 58
- dip: 36
- research_passed: 17

Warning: 752 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
