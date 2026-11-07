# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T21:49:54Z. Bankroll cash (research-selected trades): 499.4001435479087. Open positions: 25. Pools on watchlist: 58.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1053 | 13% | -61.3% | -65 to -58 | -64620 |
| all momentum | 1067 | 13% | -60.9% | -64 to -57 | -65121 |
| control | 1369 | 6% | -19.7% | -22 to -18 | -27066 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 53 | 49% | -15.3% | -29 to -2 | -818 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1046, 13%) | -20% (1369, 6%) | -41% (11, 9%) | -15% (53, 49%) |
| wide_sl50_tp100 | -61% (1046, 15%) | -20% (1369, 6%) | -48% (11, 9%) | -15% (53, 49%) |
| sl30_tp50 | -63% (1046, 16%) | -20% (1369, 7%) | -44% (11, 9%) | -17% (53, 49%) |
| sl50_tp50 | -62% (1046, 18%) | -20% (1369, 7%) | -52% (11, 9%) | -17% (53, 49%) |
| no_stop_tp100 | -61% (1046, 16%) | -20% (1369, 7%) | -45% (11, 9%) | -15% (53, 49%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 37688. Outcomes:

- missed_window: 24538
- low_liquidity: 6668
- proven_liquidity_gone: 2938
- no_momentum: 1432
- research_failed: 1057
- simulated failed buy: 462
- proven_low_volume: 428
- proven_price_collapsed_or_parabolic: 61
- proven: 55
- proven_no_uptrend: 24
- research_passed: 14
- dip: 11

Warning: 291 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
