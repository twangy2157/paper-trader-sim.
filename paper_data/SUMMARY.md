# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T09:26:39Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 13. Pools on watchlist: 40.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 826 | 14% | -58.9% | -63 to -54 | -48724 |
| all momentum | 835 | 14% | -58.7% | -63 to -54 | -49074 |
| control | 976 | 7% | -20.0% | -22 to -18 | -19597 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 41 | 46% | -14.7% | -30 to 0 | -607 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (814, 14%) | -20% (976, 7%) | -36% (8, 12%) | -15% (41, 46%) |
| wide_sl50_tp100 | -59% (814, 16%) | -20% (976, 7%) | -40% (8, 12%) | -15% (41, 46%) |
| sl30_tp50 | -61% (814, 17%) | -20% (976, 8%) | -40% (8, 12%) | -17% (41, 46%) |
| sl50_tp50 | -60% (814, 19%) | -21% (976, 8%) | -44% (8, 12%) | -17% (41, 46%) |
| no_stop_tp100 | -59% (814, 17%) | -21% (976, 7%) | -36% (8, 12%) | -15% (41, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 28973. Outcomes:

- missed_window: 18871
- low_liquidity: 5284
- proven_liquidity_gone: 2204
- no_momentum: 1029
- research_failed: 830
- simulated failed buy: 340
- proven_low_volume: 281
- proven_price_collapsed_or_parabolic: 54
- proven: 41
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 219 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
