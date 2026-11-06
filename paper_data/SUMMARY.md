# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T09:04:54Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 22. Pools on watchlist: 59.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 819 | 14% | -59.0% | -63 to -55 | -48372 |
| all momentum | 828 | 14% | -58.8% | -63 to -55 | -48722 |
| control | 972 | 7% | -19.9% | -22 to -17 | -19385 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -613 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (807, 14%) | -20% (972, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -59% (807, 16%) | -20% (972, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -61% (807, 17%) | -20% (972, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -60% (807, 19%) | -21% (972, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -59% (807, 17%) | -21% (972, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 28871. Outcomes:

- missed_window: 18800
- low_liquidity: 5268
- proven_liquidity_gone: 2193
- no_momentum: 1026
- research_failed: 830
- simulated failed buy: 339
- proven_low_volume: 281
- proven_price_collapsed_or_parabolic: 54
- proven: 41
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 218 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
