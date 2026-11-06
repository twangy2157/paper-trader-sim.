# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T21:40:12Z. Bankroll cash (research-selected trades): 706.1731051473196. Open positions: 26. Pools on watchlist: 64.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 11 | 27% | -26.5% | -63 to 13 | -294 |
| momentum, not picked | 877 | 13% | -60.1% | -64 to -56 | -52811 |
| all momentum | 888 | 14% | -59.7% | -64 to -56 | -53104 |
| control | 1085 | 6% | -19.8% | -22 to -18 | -21581 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 45 | 47% | -15.0% | -30 to -1 | -678 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (867, 14%) | -20% (1085, 6%) | -43% (9, 11%) | -15% (45, 47%) |
| wide_sl50_tp100 | -60% (867, 15%) | -20% (1085, 7%) | -47% (9, 11%) | -15% (45, 47%) |
| sl30_tp50 | -62% (867, 16%) | -20% (1085, 7%) | -47% (9, 11%) | -17% (45, 47%) |
| sl50_tp50 | -61% (867, 19%) | -21% (1085, 8%) | -50% (9, 11%) | -17% (45, 47%) |
| no_stop_tp100 | -60% (867, 16%) | -21% (1085, 7%) | -43% (9, 11%) | -15% (45, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 31020. Outcomes:

- missed_window: 20150
- low_liquidity: 5643
- proven_liquidity_gone: 2366
- no_momentum: 1148
- research_failed: 883
- simulated failed buy: 377
- proven_low_volume: 309
- proven_price_collapsed_or_parabolic: 56
- proven: 46
- proven_no_uptrend: 22
- research_passed: 11
- dip: 9

Warning: 240 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
