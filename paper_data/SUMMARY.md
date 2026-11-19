# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-19T04:33:33Z. Bankroll cash (research-selected trades): 549.3536238229275. Open positions: 20. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 17 | 29% | -26.4% | -58 to 8 | -451 |
| momentum, not picked | 3136 | 11% | -66.9% | -69 to -65 | -210157 |
| all momentum | 3153 | 11% | -66.7% | -69 to -65 | -210608 |
| control | 3863 | 6% | -19.1% | -20 to -18 | -74097 |
| dip buy | 41 | 27% | -12.0% | -29 to 6 | -494 |
| proven pools | 121 | 33% | -32.4% | -42 to -23 | -3934 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -67% (3132, 11%) | -19% (3863, 6%) | -12% (41, 27%) | -32% (121, 33%) |
| wide_sl50_tp100 | -67% (3132, 13%) | -19% (3863, 6%) | -15% (41, 29%) | -34% (121, 33%) |
| sl30_tp50 | -68% (3132, 14%) | -19% (3863, 7%) | -18% (41, 29%) | -32% (121, 34%) |
| sl50_tp50 | -68% (3132, 15%) | -20% (3863, 7%) | -19% (41, 34%) | -34% (121, 34%) |
| no_stop_tp100 | -66% (3132, 13%) | -20% (3863, 7%) | -13% (41, 29%) | -34% (121, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 104517. Outcomes:

- missed_window: 67921
- low_liquidity: 17450
- proven_liquidity_gone: 9019
- no_momentum: 3916
- research_failed: 3147
- proven_low_volume: 1355
- simulated failed buy: 1316
- proven_price_collapsed_or_parabolic: 153
- proven: 121
- proven_no_uptrend: 61
- dip: 41
- research_passed: 17

Warning: 832 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
