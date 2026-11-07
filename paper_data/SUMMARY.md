# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T19:32:09Z. Bankroll cash (research-selected trades): 499.4001435479087. Open positions: 15. Pools on watchlist: 72.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1041 | 13% | -60.9% | -64 to -57 | -63513 |
| all momentum | 1055 | 13% | -60.6% | -64 to -57 | -64014 |
| control | 1326 | 6% | -20.0% | -22 to -18 | -26589 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 53 | 49% | -15.3% | -29 to -2 | -818 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1034, 13%) | -20% (1326, 6%) | -41% (11, 9%) | -15% (53, 49%) |
| wide_sl50_tp100 | -61% (1034, 15%) | -20% (1326, 6%) | -48% (11, 9%) | -15% (53, 49%) |
| sl30_tp50 | -62% (1034, 16%) | -20% (1326, 7%) | -44% (11, 9%) | -17% (53, 49%) |
| sl50_tp50 | -62% (1034, 18%) | -21% (1326, 7%) | -52% (11, 9%) | -17% (53, 49%) |
| no_stop_tp100 | -61% (1034, 16%) | -21% (1326, 7%) | -45% (11, 9%) | -15% (53, 49%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 36871. Outcomes:

- missed_window: 23926
- low_liquidity: 6607
- proven_liquidity_gone: 2889
- no_momentum: 1381
- research_failed: 1044
- simulated failed buy: 451
- proven_low_volume: 410
- proven_price_collapsed_or_parabolic: 60
- proven: 54
- proven_no_uptrend: 24
- research_passed: 14
- dip: 11

Warning: 281 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
