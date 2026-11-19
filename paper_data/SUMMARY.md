# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-19T17:46:20Z. Bankroll cash (research-selected trades): 548.8536238229275. Open positions: 34. Pools on watchlist: 52.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3168 | 11% | -67.1% | -69 to -65 | -213021 |
| all momentum | 3185 | 11% | -66.9% | -69 to -65 | -213472 |
| control | 3897 | 6% | -19.1% | -20 to -18 | -74885 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3164, 11%) | -19% (3897, 6%) | -12% (41, 27%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3164, 13%) | -19% (3897, 7%) | -15% (41, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3164, 13%) | -19% (3897, 7%) | -18% (41, 29%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3164, 15%) | -20% (3897, 8%) | -19% (41, 34%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3164, 13%) | -20% (3897, 7%) | -13% (41, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 105403. Outcomes:

- missed_window: 68498
- low_liquidity: 17618
- proven_liquidity_gone: 9064
- no_momentum: 3956
- research_failed: 3187
- proven_low_volume: 1361
- simulated failed buy: 1323
- proven_price_collapsed_or_parabolic: 154
- proven: 123
- proven_no_uptrend: 61
- dip: 41
- research_passed: 17

Warning: 836 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
