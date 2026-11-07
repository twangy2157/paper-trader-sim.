# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T00:02:40Z. Bankroll cash (research-selected trades): 606.1731051473196. Open positions: 20. Pools on watchlist: 69.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 11 | 27% | -26.5% | -63 to 13 | -294 |
| momentum, not picked | 899 | 13% | -60.2% | -64 to -56 | -54243 |
| all momentum | 910 | 13% | -59.8% | -64 to -56 | -54536 |
| control | 1118 | 6% | -20.0% | -22 to -18 | -22414 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (889, 14%) | -20% (1118, 6%) | -43% (9, 11%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (889, 15%) | -20% (1118, 7%) | -47% (9, 11%) | -15% (46, 46%) |
| sl30_tp50 | -62% (889, 16%) | -20% (1118, 7%) | -47% (9, 11%) | -17% (46, 46%) |
| sl50_tp50 | -61% (889, 18%) | -21% (1118, 8%) | -50% (9, 11%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (889, 16%) | -21% (1118, 7%) | -43% (9, 11%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 31712. Outcomes:

- missed_window: 20551
- low_liquidity: 5801
- proven_liquidity_gone: 2418
- no_momentum: 1176
- research_failed: 904
- simulated failed buy: 388
- proven_low_volume: 328
- proven_price_collapsed_or_parabolic: 57
- proven: 46
- proven_no_uptrend: 22
- research_passed: 12
- dip: 9

Warning: 245 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
