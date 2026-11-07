# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-07T20:15:42Z. Bankroll cash (research-selected trades): 499.4001435479087. Open positions: 38. Pools on watchlist: 60.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 14 | 21% | -35.6% | -66 to -4 | -501 |
| momentum, not picked | 1042 | 13% | -61.0% | -65 to -57 | -63613 |
| all momentum | 1056 | 13% | -60.6% | -64 to -57 | -64114 |
| control | 1330 | 6% | -19.9% | -22 to -18 | -26616 |
| dip buy | 11 | 9% | -40.6% | -69 to -11 | -447 |
| proven pools | 53 | 49% | -15.3% | -29 to -2 | -818 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -61% (1035, 13%) | -20% (1330, 6%) | -41% (11, 9%) | -15% (53, 49%) |
| wide_sl50_tp100 | -61% (1035, 15%) | -20% (1330, 7%) | -48% (11, 9%) | -15% (53, 49%) |
| sl30_tp50 | -62% (1035, 16%) | -20% (1330, 7%) | -44% (11, 9%) | -17% (53, 49%) |
| sl50_tp50 | -62% (1035, 18%) | -21% (1330, 7%) | -52% (11, 9%) | -17% (53, 49%) |
| no_stop_tp100 | -61% (1035, 16%) | -21% (1330, 7%) | -45% (11, 9%) | -15% (53, 49%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 37134. Outcomes:

- missed_window: 24101
- low_liquidity: 6637
- proven_liquidity_gone: 2908
- no_momentum: 1403
- research_failed: 1050
- simulated failed buy: 458
- proven_low_volume: 414
- proven_price_collapsed_or_parabolic: 60
- proven: 54
- proven_no_uptrend: 24
- research_passed: 14
- dip: 11

Warning: 287 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
