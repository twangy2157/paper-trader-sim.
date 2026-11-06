# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T04:18:00Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 17. Pools on watchlist: 65.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 784 | 14% | -58.7% | -63 to -54 | -46103 |
| all momentum | 793 | 14% | -58.5% | -63 to -54 | -46453 |
| control | 932 | 7% | -19.4% | -22 to -17 | -18183 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (772, 14%) | -19% (932, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -59% (772, 16%) | -20% (932, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (772, 17%) | -20% (932, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -60% (772, 19%) | -20% (932, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -59% (772, 17%) | -20% (932, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 27644. Outcomes:

- missed_window: 17999
- low_liquidity: 5063
- proven_liquidity_gone: 2072
- no_momentum: 986
- research_failed: 791
- simulated failed buy: 325
- proven_low_volume: 276
- proven_price_collapsed_or_parabolic: 53
- proven: 40
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 208 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
