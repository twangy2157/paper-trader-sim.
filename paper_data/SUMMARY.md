# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T20:37:30Z. Bankroll cash (research-selected trades): 499.4001435479087. Open positions: 40. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1044 | 13% | -61.0% | -65 to -57 | -63814 |
| all momentum | 1058 | 13% | -60.7% | -64 to -57 | -64315 |
| control | 1337 | 6% | -19.9% | -22 to -18 | -26664 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 53 | 49% | -15.3% | -29 to -2 | -818 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1037, 13%) | -20% (1337, 6%) | -41% (11, 9%) | -15% (53, 49%) |
| wide_sl50_tp100 | -61% (1037, 15%) | -20% (1337, 7%) | -48% (11, 9%) | -15% (53, 49%) |
| sl30_tp50 | -62% (1037, 16%) | -20% (1337, 7%) | -44% (11, 9%) | -17% (53, 49%) |
| sl50_tp50 | -62% (1037, 18%) | -20% (1337, 7%) | -52% (11, 9%) | -17% (53, 49%) |
| no_stop_tp100 | -61% (1037, 16%) | -21% (1337, 7%) | -45% (11, 9%) | -15% (53, 49%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 37247. Outcomes:

- missed_window: 24183
- low_liquidity: 6650
- proven_liquidity_gone: 2913
- no_momentum: 1411
- research_failed: 1053
- simulated failed buy: 460
- proven_low_volume: 414
- proven_price_collapsed_or_parabolic: 60
- proven: 54
- proven_no_uptrend: 24
- research_passed: 14
- dip: 11

Warning: 289 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
