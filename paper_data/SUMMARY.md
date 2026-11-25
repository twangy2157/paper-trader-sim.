# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-25T10:21:31Z. Bankroll cash (research-selected trades): 611.9691884226207. Open positions: 31. Pools on watchlist: 66.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 23 | 35% | -16.7% | -44 to 11 | -388 |
| momentum, not picked | 3767 | 12% | -65.7% | -68 to -64 | -247778 |
| all momentum | 3790 | 12% | -65.4% | -67 to -64 | -248166 |
| control | 4527 | 6% | -19.4% | -20 to -18 | -88039 |
| dip buy | 47 | 28% | -12.8% | -30 to 4 | -606 |
| proven pools | 134 | 33% | -30.7% | -39 to -22 | -4122 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -66% (3769, 12%) | -19% (4527, 6%) | -13% (47, 28%) | -31% (134, 33%) |
| wide_sl50_tp100 | -65% (3769, 13%) | -20% (4527, 6%) | -13% (47, 32%) | -32% (134, 33%) |
| sl30_tp50 | -67% (3769, 14%) | -19% (4527, 7%) | -17% (47, 34%) | -31% (134, 34%) |
| sl50_tp50 | -67% (3769, 15%) | -20% (4527, 8%) | -18% (47, 38%) | -32% (134, 34%) |
| no_stop_tp100 | -65% (3769, 14%) | -20% (4527, 7%) | -12% (47, 32%) | -32% (134, 33%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 122233. Outcomes:

- missed_window: 78847
- low_liquidity: 20968
- proven_liquidity_gone: 10512
- no_momentum: 4588
- research_failed: 3781
- simulated failed buy: 1551
- proven_low_volume: 1547
- proven_price_collapsed_or_parabolic: 168
- proven: 134
- proven_no_uptrend: 67
- dip: 47
- research_passed: 23

Warning: 959 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
