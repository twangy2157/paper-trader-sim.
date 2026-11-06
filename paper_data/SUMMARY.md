# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-06T03:56:31Z. Bankroll cash (research-selected trades): 649.8381952860861. Open positions: 19. Pools on watchlist: 45.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 9 | 22% | -38.7% | -74 to -0 | -350 |
| momentum, not picked | 781 | 14% | -58.6% | -63 to -54 | -45803 |
| all momentum | 790 | 14% | -58.3% | -63 to -54 | -46153 |
| control | 929 | 7% | -19.5% | -22 to -17 | -18161 |
| dip buy | 8 | 12% | -36.3% | -72 to 3 | -290 |
| proven pools | 40 | 45% | -15.2% | -31 to 0 | -612 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -59% (769, 14%) | -19% (929, 7%) | -36% (8, 12%) | -15% (40, 45%) |
| wide_sl50_tp100 | -59% (769, 16%) | -20% (929, 7%) | -40% (8, 12%) | -15% (40, 45%) |
| sl30_tp50 | -60% (769, 17%) | -20% (929, 8%) | -40% (8, 12%) | -18% (40, 45%) |
| sl50_tp50 | -60% (769, 20%) | -20% (929, 8%) | -44% (8, 12%) | -18% (40, 45%) |
| no_stop_tp100 | -58% (769, 17%) | -20% (929, 7%) | -36% (8, 12%) | -15% (40, 45%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 27534. Outcomes:

- missed_window: 17927
- low_liquidity: 5044
- proven_liquidity_gone: 2059
- no_momentum: 985
- research_failed: 788
- simulated failed buy: 324
- proven_low_volume: 276
- proven_price_collapsed_or_parabolic: 52
- proven: 40
- proven_no_uptrend: 22
- research_passed: 9
- dip: 8

Warning: 208 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
