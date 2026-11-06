# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T05:21:44Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 16. Pools on watchlist: 75.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 791 | 14% | -58.6% | -63 to -54 | -46394 |
| all momentum | 800 | 14% | -58.3% | -63 to -54 | -46744 |
| control | 943 | 7% | -19.6% | -22 to -17 | -18584 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (779, 14%) | -20% (943, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -59% (779, 16%) | -20% (943, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (779, 17%) | -20% (943, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -60% (779, 20%) | -20% (943, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (779, 17%) | -20% (943, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 27942. Outcomes:

- missed_window: 18187
- low_liquidity: 5130
- proven_liquidity_gone: 2094
- no_momentum: 992
- research_failed: 802
- simulated failed buy: 328
- proven_low_volume: 277
- proven_price_collapsed_or_parabolic: 53
- proven: 40
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 209 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
