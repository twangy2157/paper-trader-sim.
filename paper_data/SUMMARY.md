# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T05:10:31Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 14. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 790 | 14% | -58.5% | -63 to -55 | -46294 |
| all momentum | 799 | 14% | -58.3% | -62 to -54 | -46644 |
| control | 942 | 7% | -19.6% | -22 to -17 | -18573 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (778, 14%) | -20% (942, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -59% (778, 16%) | -20% (942, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (778, 17%) | -20% (942, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -60% (778, 20%) | -20% (942, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (778, 17%) | -20% (942, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 27891. Outcomes:

- missed_window: 18154
- low_liquidity: 5123
- proven_liquidity_gone: 2087
- no_momentum: 991
- research_failed: 799
- simulated failed buy: 328
- proven_low_volume: 277
- proven_price_collapsed_or_parabolic: 53
- proven: 40
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 209 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
