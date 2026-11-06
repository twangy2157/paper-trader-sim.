# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T08:10:11Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 22. Pools on watchlist: 43.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 812 | 14% | -58.8% | -63 to -55 | -47825 |
| all momentum | 821 | 14% | -58.6% | -63 to -54 | -48175 |
| control | 963 | 7% | -19.7% | -22 to -17 | -19060 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -613 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (800, 14%) | -20% (963, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -59% (800, 16%) | -20% (963, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (800, 17%) | -20% (963, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -60% (800, 19%) | -20% (963, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (800, 17%) | -21% (963, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 28643. Outcomes:

- missed_window: 18655
- low_liquidity: 5223
- proven_liquidity_gone: 2175
- no_momentum: 1017
- research_failed: 823
- simulated failed buy: 335
- proven_low_volume: 281
- proven_price_collapsed_or_parabolic: 54
- proven: 41
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 216 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
