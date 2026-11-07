# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T01:04:00Z. Bankroll cash (research-selected trades): 606.1731051473196. Open positions: 17. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 11 | 27% | -26.5% | -63 to 13 | -294 |
| momentum, not picked | 902 | 13% | -60.0% | -64 to -56 | -54183 |
| all momentum | 913 | 14% | -59.6% | -63 to -56 | -54477 |
| control | 1129 | 6% | -19.9% | -22 to -18 | -22516 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (892, 14%) | -20% (1129, 6%) | -43% (9, 11%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (892, 15%) | -20% (1129, 7%) | -47% (9, 11%) | -15% (46, 46%) |
| sl30_tp50 | -62% (892, 16%) | -20% (1129, 7%) | -47% (9, 11%) | -17% (46, 46%) |
| sl50_tp50 | -61% (892, 19%) | -20% (1129, 8%) | -50% (9, 11%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (892, 16%) | -21% (1129, 7%) | -43% (9, 11%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 31942. Outcomes:

- missed_window: 20709
- low_liquidity: 5831
- proven_liquidity_gone: 2436
- no_momentum: 1184
- research_failed: 907
- simulated failed buy: 395
- proven_low_volume: 334
- proven_price_collapsed_or_parabolic: 57
- proven: 46
- proven_no_uptrend: 22
- research_passed: 12
- dip: 9

Warning: 250 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
