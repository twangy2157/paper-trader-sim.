# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T23:41:45Z. Bankroll cash (research-selected trades): 706.1731051473196. Open positions: 18. Pools on watchlist: 69.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 11 | 27% | -26.5% | -63 to 13 | -294 |
| momentum, not picked | 894 | 13% | -60.2% | -64 to -56 | -53929 |
| all momentum | 905 | 13% | -59.8% | -64 to -56 | -54223 |
| control | 1115 | 6% | -19.9% | -22 to -18 | -22299 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (884, 14%) | -20% (1115, 6%) | -43% (9, 11%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (884, 15%) | -20% (1115, 7%) | -47% (9, 11%) | -15% (46, 46%) |
| sl30_tp50 | -62% (884, 16%) | -20% (1115, 7%) | -47% (9, 11%) | -17% (46, 46%) |
| sl50_tp50 | -61% (884, 18%) | -21% (1115, 8%) | -50% (9, 11%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (884, 16%) | -21% (1115, 7%) | -43% (9, 11%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 31589. Outcomes:

- missed_window: 20471
- low_liquidity: 5781
- proven_liquidity_gone: 2408
- no_momentum: 1169
- research_failed: 902
- simulated failed buy: 387
- proven_low_volume: 326
- proven_price_collapsed_or_parabolic: 57
- proven: 46
- proven_no_uptrend: 22
- research_passed: 11
- dip: 9

Warning: 244 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
