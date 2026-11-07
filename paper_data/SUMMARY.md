# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T02:48:10Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 30. Pools on watchlist: 52.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 910 | 13% | -60.1% | -64 to -56 | -54790 |
| all momentum | 922 | 14% | -59.8% | -63 to -56 | -55185 |
| control | 1148 | 6% | -19.7% | -22 to -18 | -22738 |
| dip buy | 9 | 11% | -43.3% | -77 to -6 | -391 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (901, 14%) | -20% (1148, 6%) | -43% (9, 11%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (901, 15%) | -20% (1148, 7%) | -47% (9, 11%) | -15% (46, 46%) |
| sl30_tp50 | -62% (901, 16%) | -20% (1148, 7%) | -47% (9, 11%) | -17% (46, 46%) |
| sl50_tp50 | -61% (901, 19%) | -20% (1148, 8%) | -50% (9, 11%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (901, 16%) | -21% (1148, 7%) | -43% (9, 11%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 32449. Outcomes:

- missed_window: 21038
- low_liquidity: 5910
- proven_liquidity_gone: 2474
- no_momentum: 1209
- research_failed: 922
- simulated failed buy: 400
- proven_low_volume: 349
- proven_price_collapsed_or_parabolic: 57
- proven: 46
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 254 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
