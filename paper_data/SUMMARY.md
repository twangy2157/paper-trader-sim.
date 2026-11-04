# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T16:35:43Z. Bankroll cash (research-selected trades): 752.0843857041315. Open positions: 11. Pools on watchlist: 31.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 3 | 0% | -48.8% | - | -148 |
| momentum, not picked | 501 | 15% | -54.0% | -59 to -49 | -27105 |
| all momentum | 504 | 15% | -54.0% | -59 to -49 | -27253 |
| control | 601 | 7% | -18.8% | -22 to -16 | -11329 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 27 | 41% | -15.9% | -35 to 2 | -431 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (483, 16%) | -19% (601, 7%) | -13% (4, 25%) | -16% (27, 41%) |
| wide_sl50_tp100 | -54% (483, 18%) | -19% (601, 7%) | -13% (4, 25%) | -16% (27, 41%) |
| sl30_tp50 | -57% (483, 19%) | -19% (601, 8%) | -22% (4, 25%) | -18% (27, 41%) |
| sl50_tp50 | -56% (483, 21%) | -19% (601, 9%) | -22% (4, 25%) | -18% (27, 41%) |
| no_stop_tp100 | -54% (483, 19%) | -20% (601, 7%) | -13% (4, 25%) | -16% (27, 41%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 18605. Outcomes:

- missed_window: 12325
- low_liquidity: 3456
- proven_liquidity_gone: 1196
- no_momentum: 649
- research_failed: 505
- simulated failed buy: 212
- proven_low_volume: 175
- proven_price_collapsed_or_parabolic: 35
- proven: 29
- proven_no_uptrend: 15
- research_passed: 4
- dip: 4

Warning: 141 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
