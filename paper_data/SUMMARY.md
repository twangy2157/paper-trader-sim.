# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T11:07:43Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 34. Pools on watchlist: 44.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 833 | 14% | -59.1% | -63 to -55 | -49289 |
| all momentum | 842 | 14% | -58.9% | -63 to -55 | -49639 |
| control | 990 | 7% | -20.2% | -23 to -18 | -20076 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 41 | 46% | -14.7% | -30 to 0 | -608 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (821, 14%) | -20% (990, 7%) | -36% (8, 12%) | -15% (41, 46%) |
| wide_sl50_tp100 | -59% (821, 16%) | -21% (990, 7%) | -40% (8, 12%) | -15% (41, 46%) |
| sl30_tp50 | -61% (821, 17%) | -21% (990, 8%) | -40% (8, 12%) | -17% (41, 46%) |
| sl50_tp50 | -60% (821, 19%) | -21% (990, 8%) | -44% (8, 12%) | -17% (41, 46%) |
| no_stop_tp100 | -59% (821, 17%) | -21% (990, 7%) | -36% (8, 12%) | -15% (41, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 29388. Outcomes:

- missed_window: 19127
- low_liquidity: 5348
- proven_liquidity_gone: 2247
- no_momentum: 1051
- research_failed: 847
- simulated failed buy: 348
- proven_low_volume: 283
- proven_price_collapsed_or_parabolic: 54
- proven: 44
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 221 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
