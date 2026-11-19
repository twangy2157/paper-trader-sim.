# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-19T03:51:09Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 17. Pools on watchlist: 73.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3130 | 11% | -67.0% | -69 to -65 | -209906 |
| all momentum | 3147 | 11% | -66.8% | -69 to -65 | -210356 |
| control | 3857 | 6% | -19.1% | -20 to -18 | -73974 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 121 | 33% | -32.4% | -42 to -23 | -3934 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3126, 11%) | -19% (3857, 6%) | -12% (41, 27%) | -32% (121, 33%) |
| wide_sl50_tp100 | -67% (3126, 13%) | -19% (3857, 6%) | -15% (41, 29%) | -34% (121, 33%) |
| sl30_tp50 | -68% (3126, 14%) | -19% (3857, 7%) | -18% (41, 29%) | -32% (121, 34%) |
| sl50_tp50 | -68% (3126, 15%) | -20% (3857, 7%) | -19% (41, 34%) | -34% (121, 34%) |
| no_stop_tp100 | -67% (3126, 13%) | -20% (3857, 7%) | -13% (41, 29%) | -34% (121, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 104311. Outcomes:

- missed_window: 67782
- low_liquidity: 17412
- proven_liquidity_gone: 9008
- no_momentum: 3910
- research_failed: 3138
- proven_low_volume: 1354
- simulated failed buy: 1314
- proven_price_collapsed_or_parabolic: 153
- proven: 121
- proven_no_uptrend: 61
- dip: 41
- research_passed: 17

Warning: 831 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
