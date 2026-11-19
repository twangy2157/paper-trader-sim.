# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-19T19:44:12Z. Bankroll cash (research-selected trades): 448.8536238229275. Open positions: 24. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3192 | 11% | -67.1% | -69 to -65 | -214489 |
| all momentum | 3209 | 11% | -66.9% | -69 to -65 | -214940 |
| control | 3915 | 6% | -19.1% | -20 to -18 | -75261 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3188, 11%) | -19% (3915, 6%) | -12% (41, 27%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3188, 13%) | -19% (3915, 7%) | -15% (41, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3188, 14%) | -19% (3915, 7%) | -18% (41, 29%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3188, 15%) | -19% (3915, 8%) | -19% (41, 34%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3188, 13%) | -20% (3915, 7%) | -13% (41, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 105933. Outcomes:

- missed_window: 68846
- low_liquidity: 17704
- proven_liquidity_gone: 9111
- no_momentum: 3969
- research_failed: 3205
- proven_low_volume: 1369
- simulated failed buy: 1329
- proven_price_collapsed_or_parabolic: 157
- proven: 123
- proven_no_uptrend: 61
- dip: 41
- research_passed: 18

Warning: 839 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
