# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T17:15:39Z. Bankroll cash (research-selected trades): 472.1048725040199. Open positions: 27. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 13 | 23% | -32.8% | -65 to 3 | -428 |
| momentum, not picked | 1021 | 13% | -61.2% | -65 to -58 | -62564 |
| all momentum | 1034 | 13% | -60.8% | -64 to -57 | -62991 |
| control | 1300 | 6% | -19.9% | -22 to -18 | -25953 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 53 | 49% | -15.3% | -29 to -2 | -818 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1013, 13%) | -20% (1300, 6%) | -40% (10, 10%) | -15% (53, 49%) |
| wide_sl50_tp100 | -61% (1013, 15%) | -20% (1300, 7%) | -43% (10, 10%) | -15% (53, 49%) |
| sl30_tp50 | -62% (1013, 16%) | -20% (1300, 7%) | -44% (10, 10%) | -17% (53, 49%) |
| sl50_tp50 | -62% (1013, 18%) | -20% (1300, 7%) | -47% (10, 10%) | -17% (53, 49%) |
| no_stop_tp100 | -61% (1013, 16%) | -21% (1300, 7%) | -40% (10, 10%) | -15% (53, 49%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 36244. Outcomes:

- missed_window: 23479
- low_liquidity: 6534
- proven_liquidity_gone: 2832
- no_momentum: 1357
- research_failed: 1034
- simulated failed buy: 445
- proven_low_volume: 402
- proven_price_collapsed_or_parabolic: 60
- proven: 53
- proven_no_uptrend: 24
- research_passed: 14
- dip: 10

Warning: 280 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
