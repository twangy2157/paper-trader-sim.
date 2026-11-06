# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T10:56:29Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 25. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 833 | 14% | -59.1% | -63 to -55 | -49289 |
| all momentum | 842 | 14% | -58.9% | -63 to -55 | -49639 |
| control | 989 | 7% | -20.1% | -23 to -18 | -19975 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 41 | 46% | -14.7% | -30 to 0 | -608 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (821, 14%) | -20% (989, 7%) | -36% (8, 12%) | -15% (41, 46%) |
| wide_sl50_tp100 | -59% (821, 16%) | -21% (989, 7%) | -40% (8, 12%) | -15% (41, 46%) |
| sl30_tp50 | -61% (821, 17%) | -21% (989, 8%) | -40% (8, 12%) | -17% (41, 46%) |
| sl50_tp50 | -60% (821, 19%) | -21% (989, 8%) | -44% (8, 12%) | -17% (41, 46%) |
| no_stop_tp100 | -59% (821, 17%) | -21% (989, 7%) | -36% (8, 12%) | -15% (41, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 29348. Outcomes:

- missed_window: 19104
- low_liquidity: 5344
- proven_liquidity_gone: 2246
- no_momentum: 1047
- research_failed: 841
- simulated failed buy: 346
- proven_low_volume: 283
- proven_price_collapsed_or_parabolic: 54
- proven: 44
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 219 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
