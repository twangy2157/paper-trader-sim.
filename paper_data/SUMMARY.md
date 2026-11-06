# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T21:51:46Z. Bankroll cash (research-selected trades): 706.1731051473196. Open positions: 21. Pools on watchlist: 91.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 11 | 27% | -26.5% | -63 to 13 | -294 |
| momentum, not picked | 880 | 13% | -60.2% | -64 to -56 | -53056 |
| all momentum | 891 | 13% | -59.8% | -64 to -56 | -53350 |
| control | 1090 | 7% | -19.8% | -22 to -18 | -21700 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 45 | 47% | -15.0% | -30 to -1 | -678 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (870, 14%) | -20% (1090, 7%) | -43% (9, 11%) | -15% (45, 47%) |
| wide_sl50_tp100 | -60% (870, 15%) | -20% (1090, 7%) | -47% (9, 11%) | -15% (45, 47%) |
| sl30_tp50 | -62% (870, 16%) | -20% (1090, 7%) | -47% (9, 11%) | -17% (45, 47%) |
| sl50_tp50 | -61% (870, 19%) | -21% (1090, 8%) | -50% (9, 11%) | -17% (45, 47%) |
| no_stop_tp100 | -60% (870, 16%) | -21% (1090, 7%) | -43% (9, 11%) | -15% (45, 47%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 31080. Outcomes:

- missed_window: 20187
- low_liquidity: 5654
- proven_liquidity_gone: 2370
- no_momentum: 1148
- research_failed: 886
- simulated failed buy: 377
- proven_low_volume: 314
- proven_price_collapsed_or_parabolic: 56
- proven: 46
- proven_no_uptrend: 22
- research_passed: 11
- dip: 9

Warning: 240 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
