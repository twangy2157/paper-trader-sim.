# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T07:46:29Z. Bankroll cash (research-selected trades): 860.0946161788225. Open positions: 10. Pools on watchlist: 23.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 2 | 0% | -69.5% | - | -140 |
| momentum, not picked | 437 | 15% | -54.1% | -60 to -48 | -23685 |
| all momentum | 439 | 15% | -54.2% | -60 to -48 | -23825 |
| control | 518 | 8% | -16.7% | -20 to -14 | -8707 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 20 | 30% | -29.0% | -50 to -9 | -581 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -55% (418, 16%) | -17% (518, 8%) | -13% (4, 25%) | -29% (20, 30%) |
| wide_sl50_tp100 | -55% (418, 17%) | -17% (518, 8%) | -13% (4, 25%) | -29% (20, 30%) |
| sl30_tp50 | -57% (418, 19%) | -17% (518, 8%) | -22% (4, 25%) | -29% (20, 30%) |
| sl50_tp50 | -56% (418, 21%) | -17% (518, 9%) | -22% (4, 25%) | -29% (20, 30%) |
| no_stop_tp100 | -55% (418, 18%) | -18% (518, 8%) | -13% (4, 25%) | -29% (20, 30%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 16317. Outcomes:

- missed_window: 10844
- low_liquidity: 3091
- proven_liquidity_gone: 981
- no_momentum: 567
- research_failed: 441
- simulated failed buy: 178
- proven_low_volume: 152
- proven_price_collapsed_or_parabolic: 25
- proven: 21
- proven_no_uptrend: 11
- dip: 4
- research_passed: 2

Warning: 123 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
