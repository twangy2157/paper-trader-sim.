# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T17:59:10Z. Bankroll cash (research-selected trades): 499.4001435479087. Open positions: 27. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1029 | 13% | -60.9% | -64 to -57 | -62785 |
| all momentum | 1043 | 13% | -60.6% | -64 to -57 | -63285 |
| control | 1305 | 6% | -19.8% | -22 to -18 | -25993 |
| dip buy | 10 | 10% | -40.3% | -73 to -7 | -404 |
| proven pools | 53 | 49% | -15.3% | -29 to -2 | -818 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1022, 13%) | -20% (1305, 6%) | -40% (10, 10%) | -15% (53, 49%) |
| wide_sl50_tp100 | -61% (1022, 15%) | -20% (1305, 7%) | -43% (10, 10%) | -15% (53, 49%) |
| sl30_tp50 | -62% (1022, 16%) | -20% (1305, 7%) | -44% (10, 10%) | -17% (53, 49%) |
| sl50_tp50 | -62% (1022, 18%) | -20% (1305, 7%) | -47% (10, 10%) | -17% (53, 49%) |
| no_stop_tp100 | -61% (1022, 16%) | -21% (1305, 7%) | -40% (10, 10%) | -15% (53, 49%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 36446. Outcomes:

- missed_window: 23611
- low_liquidity: 6565
- proven_liquidity_gone: 2852
- no_momentum: 1365
- research_failed: 1039
- simulated failed buy: 446
- proven_low_volume: 406
- proven_price_collapsed_or_parabolic: 60
- proven: 53
- proven_no_uptrend: 24
- research_passed: 14
- dip: 11

Warning: 281 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
