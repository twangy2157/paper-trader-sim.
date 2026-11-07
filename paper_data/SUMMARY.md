# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T02:06:08Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 21. Pools on watchlist: 57.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 907 | 13% | -60.2% | -64 to -56 | -54684 |
| all momentum | 919 | 13% | -59.8% | -64 to -56 | -55079 |
| control | 1140 | 6% | -19.8% | -22 to -18 | -22688 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (898, 14%) | -20% (1140, 6%) | -43% (9, 11%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (898, 15%) | -20% (1140, 6%) | -47% (9, 11%) | -15% (46, 46%) |
| sl30_tp50 | -62% (898, 16%) | -20% (1140, 7%) | -47% (9, 11%) | -17% (46, 46%) |
| sl50_tp50 | -61% (898, 18%) | -20% (1140, 7%) | -50% (9, 11%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (898, 16%) | -21% (1140, 7%) | -43% (9, 11%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 32243. Outcomes:

- missed_window: 20896
- low_liquidity: 5884
- proven_liquidity_gone: 2464
- no_momentum: 1199
- research_failed: 913
- simulated failed buy: 398
- proven_low_volume: 343
- proven_price_collapsed_or_parabolic: 57
- proven: 46
- proven_no_uptrend: 22
- research_passed: 12
- dip: 9

Warning: 253 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
