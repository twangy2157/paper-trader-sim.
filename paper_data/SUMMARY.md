# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T22:02:37Z. Bankroll cash (research-selected trades): 706.1731051473196. Open positions: 20. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 11 | 27% | -26.5% | -63 to 13 | -294 |
| momentum, not picked | 881 | 13% | -60.2% | -64 to -56 | -53156 |
| all momentum | 892 | 13% | -59.8% | -64 to -56 | -53450 |
| control | 1094 | 6% | -19.8% | -22 to -18 | -21723 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 45 | 47% | -15.0% | -30 to -1 | -678 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (871, 14%) | -20% (1094, 6%) | -43% (9, 11%) | -15% (45, 47%) |
| wide_sl50_tp100 | -60% (871, 15%) | -20% (1094, 7%) | -47% (9, 11%) | -15% (45, 47%) |
| sl30_tp50 | -62% (871, 16%) | -20% (1094, 7%) | -47% (9, 11%) | -17% (45, 47%) |
| sl50_tp50 | -61% (871, 18%) | -20% (1094, 8%) | -50% (9, 11%) | -17% (45, 47%) |
| no_stop_tp100 | -60% (871, 16%) | -21% (1094, 7%) | -43% (9, 11%) | -15% (45, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 31157. Outcomes:

- missed_window: 20238
- low_liquidity: 5668
- proven_liquidity_gone: 2376
- no_momentum: 1152
- research_failed: 886
- simulated failed buy: 378
- proven_low_volume: 315
- proven_price_collapsed_or_parabolic: 56
- proven: 46
- proven_no_uptrend: 22
- research_passed: 11
- dip: 9

Warning: 240 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
