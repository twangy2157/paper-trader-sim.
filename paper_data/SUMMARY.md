# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T12:34:12Z. Bankroll cash (research-selected trades): 549.8381952860861. Open positions: 16. Pools on watchlist: 50.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 849 | 14% | -59.6% | -64 to -56 | -50675 |
| all momentum | 858 | 14% | -59.4% | -63 to -55 | -51025 |
| control | 1011 | 7% | -20.0% | -22 to -17 | -20308 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 41 | 46% | -14.7% | -30 to 0 | -608 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -60% (837, 14%) | -20% (1011, 7%) | -36% (8, 12%) | -15% (41, 46%) |
| wide_sl50_tp100 | -60% (837, 16%) | -20% (1011, 7%) | -40% (8, 12%) | -15% (41, 46%) |
| sl30_tp50 | -61% (837, 17%) | -20% (1011, 8%) | -40% (8, 12%) | -17% (41, 46%) |
| sl50_tp50 | -61% (837, 19%) | -21% (1011, 8%) | -44% (8, 12%) | -17% (41, 46%) |
| no_stop_tp100 | -59% (837, 16%) | -21% (1011, 7%) | -36% (8, 12%) | -15% (41, 46%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 29707. Outcomes:

- missed_window: 19325
- low_liquidity: 5393
- proven_liquidity_gone: 2288
- no_momentum: 1061
- research_failed: 854
- simulated failed buy: 356
- proven_low_volume: 291
- proven_price_collapsed_or_parabolic: 54
- proven: 44
- proven_no_uptrend: 22
- research_passed: 10
- dip: 9

Warning: 223 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
