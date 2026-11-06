# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T22:35:35Z. Bankroll cash (research-selected trades): 706.1731051473196. Open positions: 24. Pools on watchlist: 29.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 11 | 27% | -26.5% | -63 to 13 | -294 |
| momentum, not picked | 882 | 13% | -60.2% | -64 to -56 | -53211 |
| all momentum | 893 | 13% | -59.8% | -64 to -56 | -53505 |
| control | 1102 | 6% | -19.8% | -22 to -18 | -21899 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (872, 14%) | -20% (1102, 6%) | -43% (9, 11%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (872, 15%) | -20% (1102, 7%) | -47% (9, 11%) | -15% (46, 46%) |
| sl30_tp50 | -62% (872, 16%) | -20% (1102, 7%) | -47% (9, 11%) | -17% (46, 46%) |
| sl50_tp50 | -61% (872, 18%) | -20% (1102, 8%) | -50% (9, 11%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (872, 16%) | -21% (1102, 7%) | -43% (9, 11%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 31317. Outcomes:

- missed_window: 20341
- low_liquidity: 5697
- proven_liquidity_gone: 2384
- no_momentum: 1159
- research_failed: 893
- simulated failed buy: 379
- proven_low_volume: 319
- proven_price_collapsed_or_parabolic: 57
- proven: 46
- proven_no_uptrend: 22
- research_passed: 11
- dip: 9

Warning: 241 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
