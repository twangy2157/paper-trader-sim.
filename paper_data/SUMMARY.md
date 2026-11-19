# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-19T19:33:38Z. Bankroll cash (research-selected trades): 448.8536238229275. Open positions: 24. Pools on watchlist: 56.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3190 | 11% | -67.1% | -69 to -65 | -214288 |
| all momentum | 3207 | 11% | -66.9% | -69 to -65 | -214739 |
| control | 3913 | 6% | -19.1% | -20 to -18 | -75180 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 123 | 33% | -31.5% | -41 to -22 | -3883 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3186, 11%) | -19% (3913, 6%) | -12% (41, 27%) | -31% (123, 33%) |
| wide_sl50_tp100 | -67% (3186, 13%) | -19% (3913, 6%) | -15% (41, 29%) | -32% (123, 33%) |
| sl30_tp50 | -68% (3186, 14%) | -19% (3913, 7%) | -18% (41, 29%) | -32% (123, 34%) |
| sl50_tp50 | -68% (3186, 15%) | -19% (3913, 8%) | -19% (41, 34%) | -33% (123, 34%) |
| no_stop_tp100 | -67% (3186, 13%) | -20% (3913, 7%) | -13% (41, 29%) | -33% (123, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 105887. Outcomes:

- missed_window: 68818
- low_liquidity: 17697
- proven_liquidity_gone: 9105
- no_momentum: 3965
- research_failed: 3205
- proven_low_volume: 1369
- simulated failed buy: 1328
- proven_price_collapsed_or_parabolic: 157
- proven: 123
- proven_no_uptrend: 61
- dip: 41
- research_passed: 18

Warning: 839 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
