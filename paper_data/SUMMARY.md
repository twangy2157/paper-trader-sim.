# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T20:47:39Z. Bankroll cash (research-selected trades): 499.4001435479087. Open positions: 35. Pools on watchlist: 102.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1045 | 13% | -61.1% | -65 to -57 | -63914 |
| all momentum | 1059 | 13% | -60.7% | -64 to -57 | -64415 |
| control | 1343 | 6% | -19.8% | -22 to -18 | -26698 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 53 | 49% | -15.3% | -29 to -2 | -818 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1038, 13%) | -20% (1343, 6%) | -41% (11, 9%) | -15% (53, 49%) |
| wide_sl50_tp100 | -61% (1038, 15%) | -20% (1343, 6%) | -48% (11, 9%) | -15% (53, 49%) |
| sl30_tp50 | -62% (1038, 16%) | -20% (1343, 7%) | -44% (11, 9%) | -17% (53, 49%) |
| sl50_tp50 | -62% (1038, 18%) | -20% (1343, 7%) | -52% (11, 9%) | -17% (53, 49%) |
| no_stop_tp100 | -61% (1038, 16%) | -20% (1343, 7%) | -45% (11, 9%) | -15% (53, 49%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 37298. Outcomes:

- missed_window: 24222
- low_liquidity: 6654
- proven_liquidity_gone: 2918
- no_momentum: 1413
- research_failed: 1053
- simulated failed buy: 460
- proven_low_volume: 415
- proven_price_collapsed_or_parabolic: 60
- proven: 54
- proven_no_uptrend: 24
- research_passed: 14
- dip: 11

Warning: 289 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
