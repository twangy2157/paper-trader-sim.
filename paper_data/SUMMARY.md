# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T03:46:10Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 20. Pools on watchlist: 38.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 778 | 14% | -58.8% | -63 to -55 | -45781 |
| all momentum | 787 | 14% | -58.5% | -63 to -54 | -46131 |
| control | 927 | 7% | -19.4% | -22 to -17 | -18064 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (766, 14%) | -19% (927, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -59% (766, 16%) | -20% (927, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (766, 17%) | -20% (927, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -60% (766, 19%) | -20% (927, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -59% (766, 17%) | -20% (927, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 27500. Outcomes:

- missed_window: 17908
- low_liquidity: 5040
- proven_liquidity_gone: 2052
- no_momentum: 983
- research_failed: 786
- simulated failed buy: 324
- proven_low_volume: 276
- proven_price_collapsed_or_parabolic: 52
- proven: 40
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 208 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
