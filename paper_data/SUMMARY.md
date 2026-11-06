# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T05:00:11Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 14. Pools on watchlist: 46.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 788 | 14% | -58.4% | -63 to -54 | -46094 |
| all momentum | 797 | 14% | -58.2% | -62 to -54 | -46444 |
| control | 941 | 7% | -19.6% | -22 to -17 | -18561 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (776, 14%) | -20% (941, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -59% (776, 16%) | -20% (941, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (776, 18%) | -20% (941, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -60% (776, 20%) | -20% (941, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (776, 17%) | -21% (941, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 27852. Outcomes:

- missed_window: 18134
- low_liquidity: 5114
- proven_liquidity_gone: 2082
- no_momentum: 990
- research_failed: 797
- simulated failed buy: 327
- proven_low_volume: 276
- proven_price_collapsed_or_parabolic: 53
- proven: 40
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 208 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
