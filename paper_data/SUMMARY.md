# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-03T07:29:56Z. Bankroll cash (research-selected trades): 898.0. Open positions: 7. Pools on watchlist: 61.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 1 | 0% | -101.0% | - | -102 |
| momentum, not picked | 255 | 16% | -50.7% | -59 to -43 | -12950 |
| all momentum | 256 | 16% | -50.9% | -58 to -43 | -13052 |
| control | 287 | 8% | -16.7% | -21 to -12 | -4805 |
| dip buy | 1 | 100% | 57.9% | - | 58 |
| proven pools | 5 | 20% | -79.4% | - | -397 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -52% (235, 17%) | -17% (287, 8%) | 58% (1, 100%) | -79% (5, 20%) |
| wide_sl50_tp100 | -53% (235, 18%) | -17% (287, 8%) | 58% (1, 100%) | -79% (5, 20%) |
| sl30_tp50 | -54% (235, 21%) | -18% (287, 9%) | 24% (1, 100%) | -79% (5, 20%) |
| sl50_tp50 | -53% (235, 23%) | -18% (287, 9%) | 24% (1, 100%) | -79% (5, 20%) |
| no_stop_tp100 | -53% (235, 18%) | -17% (287, 8%) | 58% (1, 100%) | -79% (5, 20%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 9723. Outcomes:

- missed_window: 6442
- low_liquidity: 2104
- proven_liquidity_gone: 392
- no_momentum: 334
- research_failed: 257
- simulated failed buy: 98
- proven_low_volume: 67
- proven_price_collapsed_or_parabolic: 11
- proven_no_uptrend: 9
- proven: 7
- research_passed: 1
- dip: 1

Warning: 64 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
