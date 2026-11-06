# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T06:25:57Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 23. Pools on watchlist: 70.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 803 | 14% | -58.7% | -63 to -54 | -47179 |
| all momentum | 812 | 14% | -58.4% | -63 to -54 | -47529 |
| control | 948 | 7% | -19.6% | -22 to -17 | -18661 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (791, 14%) | -20% (948, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -59% (791, 16%) | -20% (948, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (791, 17%) | -20% (948, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -60% (791, 19%) | -20% (948, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (791, 17%) | -20% (948, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 28270. Outcomes:

- missed_window: 18404
- low_liquidity: 5175
- proven_liquidity_gone: 2132
- no_momentum: 1006
- research_failed: 811
- simulated failed buy: 331
- proven_low_volume: 278
- proven_price_collapsed_or_parabolic: 53
- proven: 41
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 213 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
