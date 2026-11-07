# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T06:22:09Z. Bankroll cash (research-selected trades): 605.1869477321155. Open positions: 18. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 12 | 25% | -32.7% | -67 to 6 | -395 |
| momentum, not picked | 941 | 13% | -60.2% | -64 to -56 | -56756 |
| all momentum | 953 | 13% | -59.9% | -64 to -56 | -57151 |
| control | 1193 | 6% | -19.9% | -22 to -18 | -23900 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 46 | 46% | -14.8% | -29 to -1 | -684 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (932, 14%) | -20% (1193, 6%) | -40% (10, 10%) | -15% (46, 46%) |
| wide_sl50_tp100 | -60% (932, 15%) | -20% (1193, 7%) | -43% (10, 10%) | -15% (46, 46%) |
| sl30_tp50 | -62% (932, 16%) | -20% (1193, 7%) | -44% (10, 10%) | -17% (46, 46%) |
| sl50_tp50 | -61% (932, 18%) | -21% (1193, 8%) | -47% (10, 10%) | -17% (46, 46%) |
| no_stop_tp100 | -60% (932, 16%) | -21% (1193, 7%) | -40% (10, 10%) | -15% (46, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 33445. Outcomes:

- missed_window: 21696
- low_liquidity: 6059
- proven_liquidity_gone: 2563
- no_momentum: 1249
- research_failed: 945
- simulated failed buy: 414
- proven_low_volume: 369
- proven_price_collapsed_or_parabolic: 58
- proven: 48
- proven_no_uptrend: 22
- research_passed: 12
- dip: 10

Warning: 264 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
