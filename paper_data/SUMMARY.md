# Paper trader summary

SIMULATION ONLY. No real trades.

Updated 2026-11-04T23:45:08Z. Bankroll cash (research-selected trades): 816.8065461812329. Open positions: 24. Pools on watchlist: 78.

| group | n | win | avg | CI | P&L $ |
|---|---|---|---|---|---|
| research-picked | 5 | 20% | -36.3% | - | -183 |
| momentum, not picked | 551 | 16% | -53.7% | -59 to -48 | -29640 |
| all momentum | 556 | 16% | -53.6% | -58 to -48 | -29823 |
| control | 674 | 7% | -18.9% | -22 to -16 | -12824 |
| dip buy | 4 | 25% | -13.1% | - | -52 |
| proven pools | 31 | 42% | -17.5% | -35 to -1 | -545 |

What-if exit rules on the SAME trades. Cells: avg return (trades, win rate).

| exit rule | momentum | control | dip | proven |
|---|---|---|---|---|
| base_sl30_tp100 | -54% (535, 16%) | -19% (674, 7%) | -13% (4, 25%) | -18% (31, 42%) |
| wide_sl50_tp100 | -54% (535, 18%) | -19% (674, 8%) | -13% (4, 25%) | -18% (31, 42%) |
| sl30_tp50 | -55% (535, 20%) | -19% (674, 8%) | -22% (4, 25%) | -19% (31, 42%) |
| sl50_tp50 | -55% (535, 22%) | -19% (674, 9%) | -22% (4, 25%) | -19% (31, 42%) |
| no_stop_tp100 | -53% (535, 19%) | -20% (674, 8%) | -13% (4, 25%) | -18% (31, 42%) |

Verdict: NOT ENOUGH DATA (need 30+ closed filter=1 trades and a CI above zero before believing anything).

Pools seen: 20284. Outcomes:

- missed_window: 13350
- low_liquidity: 3756
- proven_liquidity_gone: 1360
- no_momentum: 735
- research_failed: 557
- simulated failed buy: 229
- proven_low_volume: 193
- proven_price_collapsed_or_parabolic: 43
- proven: 32
- proven_no_uptrend: 20
- research_passed: 5
- dip: 4

Warning: 153 judged pools had an unreadable mint/freeze value. Check mint_raw / freeze_raw in candidates.csv; the parsing may need fixing.
