# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T21:08:00Z. Bankroll cash (research-selected trades): 499.4001435479087. Open positions: 26. Pools on watchlist: 83.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1049 | 13% | -61.1% | -65 to -57 | -64220 |
| all momentum | 1063 | 13% | -60.8% | -64 to -57 | -64721 |
| control | 1353 | 6% | -19.7% | -22 to -18 | -26751 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 53 | 49% | -15.3% | -29 to -2 | -818 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1042, 13%) | -20% (1353, 6%) | -41% (11, 9%) | -15% (53, 49%) |
| wide_sl50_tp100 | -61% (1042, 15%) | -20% (1353, 7%) | -48% (11, 9%) | -15% (53, 49%) |
| sl30_tp50 | -62% (1042, 16%) | -20% (1353, 7%) | -44% (11, 9%) | -17% (53, 49%) |
| sl50_tp50 | -62% (1042, 18%) | -20% (1353, 7%) | -52% (11, 9%) | -17% (53, 49%) |
| no_stop_tp100 | -61% (1042, 16%) | -20% (1353, 7%) | -45% (11, 9%) | -15% (53, 49%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 37432. Outcomes:

- missed_window: 24338
- low_liquidity: 6656
- proven_liquidity_gone: 2927
- no_momentum: 1417
- research_failed: 1053
- simulated failed buy: 460
- proven_low_volume: 417
- proven_price_collapsed_or_parabolic: 60
- proven: 55
- proven_no_uptrend: 24
- research_passed: 14
- dip: 11

Warning: 289 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
