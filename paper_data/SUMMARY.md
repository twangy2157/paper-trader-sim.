# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-09T14:17:45Z. Bankroll cash (research-selected trades): 456.400154541351. Open positions: 22. Pools on watchlist: 54.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 16 | 25% | -33.9% | -64 to -3 | -544 |
| momentum, not picked | 1330 | 13% | -63.0% | -66 to -60 | -83975 |
| all momentum | 1346 | 13% | -62.7% | -66 to -59 | -84518 |
| control | 1855 | 5% | -18.7% | -20 to -17 | -34911 |
| dip buy | 13 | 8% | -38.7% | -63 to -14 | -504 |
| proven pools | 65 | 43% | -19.4% | -31 to -7 | -1266 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -63% (1325, 13%) | -19% (1855, 5%) | -39% (13, 8%) | -19% (65, 43%) |
| wide_sl50_tp100 | -63% (1325, 15%) | -19% (1855, 6%) | -45% (13, 8%) | -20% (65, 43%) |
| sl30_tp50 | -64% (1325, 16%) | -19% (1855, 6%) | -41% (13, 8%) | -21% (65, 43%) |
| sl50_tp50 | -63% (1325, 18%) | -19% (1855, 6%) | -48% (13, 8%) | -21% (65, 43%) |
| no_stop_tp100 | -62% (1325, 15%) | -19% (1855, 6%) | -43% (13, 8%) | -20% (65, 43%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 49557. Outcomes:

- missed_window: 32907
- low_liquidity: 8115
- proven_liquidity_gone: 3762
- no_momentum: 1907
- research_failed: 1339
- proven_low_volume: 714
- simulated failed buy: 601
- proven_price_collapsed_or_parabolic: 83
- proven: 70
- proven_no_uptrend: 30
- research_passed: 16
- dip: 13

Warning: 401 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
