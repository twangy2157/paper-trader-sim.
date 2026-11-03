# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T16:05:45Z. Bankroll cash (research-selected trades): 798.0. Open positions: 28. Pools on watchlist: 53.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 327 | 14% | -54.4% | -61 to -48 | -17832 |
| all momentum | 328 | 14% | -54.6% | -62 to -48 | -17934 |
| control | 364 | 8% | -16.2% | -20 to -12 | -5938 |
| dip buy | 2 | 50% | 24.4% | - | 49 |
| proven pools | 14 | 36% | -32.3% | -61 to -5 | -453 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -56% (307, 15%) | -16% (364, 8%) | 24% (2, 50%) | -32% (14, 36%) |
| wide_sl50_tp100 | -55% (307, 17%) | -17% (364, 9%) | 24% (2, 50%) | -32% (14, 36%) |
| sl30_tp50 | -57% (307, 20%) | -17% (364, 9%) | 7% (2, 50%) | -32% (14, 36%) |
| sl50_tp50 | -56% (307, 22%) | -17% (364, 9%) | 7% (2, 50%) | -32% (14, 36%) |
| no_stop_tp100 | -55% (307, 18%) | -17% (364, 9%) | 24% (2, 50%) | -32% (14, 36%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 12052. Outcomes:

- missed_window: 7988
- low_liquidity: 2436
- proven_liquidity_gone: 601
- no_momentum: 424
- research_failed: 336
- simulated failed buy: 123
- proven_low_volume: 99
- proven: 16
- proven_price_collapsed_or_parabolic: 16
- proven_no_uptrend: 9
- research_passed: 2
- dip: 2

Warning: 80 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
