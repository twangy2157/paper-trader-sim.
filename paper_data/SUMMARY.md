# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T07:17:00Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 11. Pools on watchlist: 47.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 809 | 14% | -58.7% | -63 to -54 | -47525 |
| all momentum | 818 | 14% | -58.4% | -62 to -54 | -47875 |
| control | 957 | 7% | -19.6% | -22 to -17 | -18875 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (797, 14%) | -20% (957, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -59% (797, 16%) | -20% (957, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (797, 17%) | -20% (957, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -60% (797, 19%) | -20% (957, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (797, 17%) | -20% (957, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 28407. Outcomes:

- missed_window: 18514
- low_liquidity: 5184
- proven_liquidity_gone: 2144
- no_momentum: 1008
- research_failed: 812
- simulated failed buy: 333
- proven_low_volume: 279
- proven_price_collapsed_or_parabolic: 53
- proven: 41
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 215 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
